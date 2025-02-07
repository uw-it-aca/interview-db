# Copyright 2025 UW-IT, University of Washington
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


class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'page_count': self.page.paginator.num_pages,
            'page_size': self.page_size,
            'page_number': self.page.number,
            'results': data,
        })


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
class InterviewListView(APIView, CustomPagination):
    """
    API endpoint returning list of interviews with pagination and filtering
    Used on students page to display all interview listings
    """
    STANDING = {
        "Freshman": "Fr",
        "Sophomore": "So",
        "Junior": "Jr",
        "Senior": "Sr",
        "Alumni - undergrad": "Al",
        "Masters": "Ma",
        "PhD": "Ph",
    }

    # helper to get all interview ids for a topic
    def get_interviews(self, topic):
        interviews = set()
        for code in topic.codes.all():
            for story in code.story_set.all():
                interviews.add(story.interview.id)
        for subcode in topic.subcodes.all():
            for story in subcode.story_set.all():
                interviews.add(story.interview.id)
        return interviews

    def get(self, request):
        queryset = Interview.objects.exclude(
            pull_quote__isnull=True).exclude(
            pull_quote__exact='').exclude(
            pull_quote__exact='0').exclude(
            signed_release_form=False).order_by('-date')

        # filter on years
        years = self.request.GET.getlist('year')
        if years is not None and len(years) > 0:
            # Senior+ filter includes PhD, Alum, Masters
            if 'Senior' in years:
                years.append("PhD")
                years.append("Alumni - undergrad")
                years.append("Masters")
            # model uses abbreviation, but query uses full title
            years_abbr = []
            for year in years:
                years_abbr.append(self.STANDING[year])
            queryset = queryset.filter(standing__in=years_abbr)

        # filter on majors
        majors = self.request.GET.getlist('major')
        if majors is not None and len(majors) > 0:
            queryset = queryset.filter(major__full_title__in=majors)

        # filter on topics
        topics = self.request.GET.getlist('topic')
        if topics is not None and len(topics) > 0:
            for topic_str in topics:
                topic = Collection.objects.get(topic=topic_str)
                interviews = self.get_interviews(topic)
                # check if interview id contained in a topic's set of ids
                queryset = queryset.filter(id__in=interviews)

        # done filtering, now paginate
        queryset = self.paginate_queryset(queryset, request, view=self)
        serializer = InterviewSerializer(
            queryset, many=True, context={"request": request})
        return self.get_paginated_response(serializer.data)


@method_decorator(group_required(front_end_group), name='dispatch')
class SingleInterviewView(APIView):
    """
    API endpoint returning single interview, made up of its matching stories
    Each story has the topics it mentions
    Used on single interview page to divide interview into filterable stories
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
class CollectionStoryView(APIView, CustomPagination):
    """
    API endpoint returning single collection of stories with
    pagination and filtering, used on topics.vue
    """
    STANDING = {
        "Freshman": "Fr",
        "Sophomore": "So",
        "Junior": "Jr",
        "Senior": "Sr",
        "Alumni - undergrad": "Al",
        "Masters": "Ma",
        "PhD": "Ph",
    }

    def get(self, request, id):
        collection = Collection.objects.get(id=id)
        queryset = Story.objects.filter(
            Q(code__in=collection.codes.all()) |
            Q(subcode__in=collection.subcodes.all())).exclude(
            interview__pull_quote__isnull=True).exclude(
            interview__pull_quote__exact='').exclude(
            interview__pull_quote__exact='0').exclude(
            interview__signed_release_form=False)

        # filter on years
        years = self.request.GET.getlist('year')
        if years is not None and len(years) > 0:
            # Senior+ filter includes PhD, Alum, Masters
            if 'Senior' in years:
                years.append("PhD")
                years.append("Alumni - undergrad")
                years.append("Masters")
            # model uses abbreviation, but query uses full title
            years_abbr = []
            for year in years:
                years_abbr.append(self.STANDING[year])
            queryset = queryset.filter(interview__standing__in=years_abbr)

        # filter on majors
        majors = self.request.GET.getlist('major')
        if majors is not None and len(majors) > 0:
            queryset = queryset.filter(interview__major__full_title__in=majors)

        queryset = self.paginate_queryset(queryset, request, view=self)
        serializer = StorySerializer(queryset, many=True)
        return self.get_paginated_response(serializer.data)


@method_decorator(group_required(front_end_group), name='dispatch')
class InterviewTopicsView(APIView):
    """
    API endpoint returning all the collections of a single interview
    Used on single interview page to display all topics mentioned
    """

    def get(self, request, id):
        interview = Story.objects.filter(interview__id=id)
        queryset = set()

        for story in interview:
            for code in story.code.all():
                for topic in code.collection_set.all():
                    queryset.add(topic)
            for code in story.subcode.all():
                for topic in code.collection_set.all():
                    queryset.add(topic)

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
