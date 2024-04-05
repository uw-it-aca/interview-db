# Copyright 2024 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.conf import settings
from django.views.generic import TemplateView
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from uw_saml.decorators import group_required
from datetime import datetime, timedelta, timezone
from .serializers import *
from .models import *

admin_group = settings.INTERVIEW_DB_AUTHZ_GROUPS['admin']
front_end_group = settings.INTERVIEW_DB_AUTHZ_GROUPS['front-end']


@method_decorator(group_required(front_end_group), name='dispatch')
class PageView(TemplateView):
    template_name = "vue.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def render_to_response(self, context, **response_kwargs):
        response = super(PageView, self).render_to_response(
            context, **response_kwargs)
        return response


@method_decorator(group_required(front_end_group), name='dispatch')
class DefaultPageView(PageView):
    template_name = "vue.html"


@method_decorator(group_required(front_end_group), name='dispatch')
class InterviewListView(APIView):
    """
    API endpoint returning list of interviews without collections
    """

    def get(self, request):
        queryset = Interview.objects.exclude(
            pull_quote__isnull=True).exclude(
            pull_quote__exact='').exclude(
            pull_quote__exact='0').exclude(
            signed_release_form=False).order_by('-date')
        serializer = InterviewSerializer(queryset, many=True,
                                         context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


@method_decorator(group_required(front_end_group), name='dispatch')
class InterviewCollectionListView(APIView, PageNumberPagination):
    """
    API endpoint returning list of interviews with their collections
    """

    def get(self, request):
        queryset = Interview.objects.exclude(
            pull_quote__isnull=True).exclude(
            pull_quote__exact='').exclude(
            pull_quote__exact='0').exclude(
            signed_release_form=False).order_by('-date')
        queryset = self.paginate_queryset(queryset, request, view=self)
        serializer = InterviewCollectionSerializer(
            queryset, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


@method_decorator(group_required(front_end_group), name='dispatch')
class InterviewDetailView(APIView):
    """
    API endpoint returning single interview, made up of its matching stories
    """

    def get(self, request, id):
        queryset = Story.objects.filter(interview__id=id)
        serializer = StoryTopicSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@method_decorator(group_required(front_end_group), name='dispatch')
class CollectionListView(APIView):
    """
    API endpoint returning list of collections
    """

    def get(self, request):
        queryset = Collection.objects.all().order_by('topic')
        serializer = CollectionSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@method_decorator(group_required(front_end_group), name='dispatch')
class CollectionInfoView(APIView):
    """
    API endpoint returning basic info of single collection without its
    stories
    """

    def get(self, request, id):
        queryset = Collection.objects.get(id=id)
        serializer = CollectionSerializer(queryset, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


@method_decorator(group_required(front_end_group), name='dispatch')
class CollectionStoryView(APIView, PageNumberPagination):
    """
    API endpoint returning single collection of stories
    """

    def get(self, request, id):
        collection = Collection.objects.get(id=id)
        queryset = Story.objects.filter(
            Q(code__in=collection.codes.all()) |
            Q(subcode__in=collection.subcodes.all())).exclude(
            interview__pull_quote__isnull=True).exclude(
            interview__pull_quote__exact='').exclude(
            interview__pull_quote__exact='0').exclude(
            interview__signed_release_form=False)
        queryset = self.paginate_queryset(queryset, request, view=self)
        serializer = StorySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@method_decorator(group_required(front_end_group), name='dispatch')
class InterviewTopicsView(APIView):
    """
    API endpoint returning all the collections of a single interview
    """

    def get(self, request, id):
        interview = Story.objects.filter(interview__id=id)
        queryset = set()
        curr_codes = set()

        for story in interview:
            for code in story.code.all():
                curr_codes.add(code)
            for code in story.subcode.all():
                curr_codes.add(code)

        for topic in Collection.objects.all():
            for code in topic.codes.all():
                if code in curr_codes:
                    queryset.add(topic)
                    continue
            for code in topic.subcodes.all():
                if code in curr_codes:
                    queryset.add(topic)
                    continue

        serializer = CollectionSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@method_decorator(group_required(front_end_group), name='dispatch')
class MajorListView(APIView):
    """
    API endpoint returning all added majors
    """

    def get(self, request):
        queryset = Major.objects.all().order_by('full_title')
        serializer = MajorSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@method_decorator(group_required(front_end_group), name='dispatch')
class RandomStudentsView(APIView):
    """
    API endpoint returning three random students
    """

    def get(self, request):
        queryset = Interview.objects.exclude(
            pull_quote__isnull=True).exclude(
            pull_quote__exact='').exclude(
            pull_quote__exact='0').exclude(
            signed_release_form=False).order_by("?")[:3]
        serializer = InterviewSerializer(queryset, many=True)
        return Response(serializer.data)


@method_decorator(group_required(front_end_group), name='dispatch')
class ImageView(APIView):
    """
    API endpoint returning images
    """

    def get(self, request, id):
        interview = Interview.objects.get(id=id)
        img = interview.image

        # check if publishable in the first place
        if interview.signed_release_form is False:
            return Response('Image not shown for privacy',
                            status=status.HTTP_400_BAD_REQUEST)

        if img == '':
            return Response('Interview has no image',
                            status=status.HTTP_400_BAD_REQUEST)

        if interview.no_identifying_photo:
            if interview.image_is_not_identifying is False:
                return Response('Image not shown for privacy',
                                status=status.HTTP_400_BAD_REQUEST)

        expires = datetime.now(timezone.utc) + timedelta(
            seconds=settings.IMAGE_CACHE_EXPIRES)

        try:
            response = HttpResponse(img, content_type='image/jpeg')
            response['Cache-Control'] = 'public,max-age={}'.format(
                settings.IMAGE_CACHE_EXPIRES)
            response['Expires'] = expires.strftime('%a, %d %b %Y %H:%M:%S GMT')
        except IOError:
            response = Response('Not found', status=status.HTTP_404_NOT_FOUND)
        return response


# include undisplayed interviews?
@method_decorator(group_required(front_end_group), name='dispatch')
class InterviewCountView(APIView):
    """
    API endpoint returning total number of interviews (displayed)
    """
    def get(self, request):
        queryset = Interview.objects.exclude(
            pull_quote__isnull=True).exclude(
            pull_quote__exact='').exclude(
            pull_quote__exact='0').exclude(
            signed_release_form=False).count()
        return Response(queryset, status=status.HTTP_200_OK)


# exclude stories from the excluded interviews?
@method_decorator(group_required(front_end_group), name='dispatch')
class StoryCountView(APIView):
    """
    API endpoint returning total number of stories
    """
    def get(self, request):
        queryset = Story.objects.all().count()
        return Response(queryset, status=status.HTTP_200_OK)
