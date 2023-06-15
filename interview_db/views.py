# Copyright 2023 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.conf import settings
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from django.utils.decorators import method_decorator
from wsgiref.util import FileWrapper
from django.http import HttpResponse
from django.core.files.images import ImageFile
from uw_saml.decorators import group_required
from .serializers import *
from .models import *
import base64

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
    API endpoint returning list of interviews
    """

    def get(self, request):
        queryset = Interview.objects.exclude(
            pull_quote__isnull=True).exclude(
            pull_quote__exact='').exclude(
            pull_quote__exact='0').order_by('-date')
        serializer = InterviewSerializer(queryset, many=True,
                                         context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


@method_decorator(group_required(front_end_group), name='dispatch')
class InterviewDetailView(APIView):
    """
    API endpoint returning single interview, made up of its matching stories
    """

    def get(self, request, id):
        queryset = Story.objects.filter(interview__id=id)
        serializer = StorySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@method_decorator(group_required(front_end_group), name='dispatch')
class CollectionListView(APIView):
    """
    API endpoint returning list of collections
    """

    def get(self, request):
        queryset = Collection.objects.all()
        serializer = CollectionSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@method_decorator(group_required(front_end_group), name='dispatch')
class CollectionInfoView(APIView):
    """
    API endpoint returning basic info of single collection
    """

    def get(self, request, id):
        queryset = Collection.objects.get(id=id)
        serializer = CollectionSerializer(queryset, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


@method_decorator(group_required(front_end_group), name='dispatch')
class CollectionStoryView(APIView):
    """
    API endpoint returning single collection of stories
    """

    def get(self, request, id):
        collection = Collection.objects.get(id=id)
        queryset = Story.objects.filter(
            Q(code__in=collection.codes.all()) |
            Q(subcode__in=collection.subcodes.all()))
        serializer = StorySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@method_decorator(group_required(front_end_group), name='dispatch')
class InterviewTopicsView(APIView):
    """
    API endpoint returning all the collections of a single interview
    """

    def get(self, request, id):
        interview = Story.objects.filter(interview__id=id)
        queryset = []
        list = []
        for s in interview:
            list.append(s.code.all())
            list.append(s.subcode.all())

        for code in list:
            for c in Collection.objects.all():
                if code[0] in c.codes.all() or code[0] in c.subcodes.all():
                    queryset.append(c)

        queryset = [*set(queryset)]
        serializer = CollectionSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@method_decorator(group_required(front_end_group), name='dispatch')
class MajorListView(APIView):
    """
    API endpoint returning all added majors
    """

    def get(self, request):
        queryset = Major.objects.all()
        serializer = MajorSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@method_decorator(group_required(front_end_group), name='dispatch')
class StudentTypeListView(APIView):
    """
    API endpoint returning all student types
    """

    def get(self, request):
        queryset = StudentType.objects.all()
        serializer = StudentTypeSerializer(queryset, many=True)
        return Response(serializer.data)


@method_decorator(group_required(front_end_group), name='dispatch')
class RandomStudentsView(APIView):
    """
    API endpoint returning three random students
    """

    def get(self, request):
        queryset = Interview.objects.order_by("?")[:3]
        serializer = InterviewSerializer(queryset, many=True)
        return Response(serializer.data)


@method_decorator(group_required(front_end_group), name='dispatch')
class RecentStudentsView(APIView):
    """
    API endpoint returning three random students
    """

    def get(self, request):
        queryset = Interview.objects.all().order_by('-date')[:3]
        serializer = InterviewSerializer(queryset, many=True,
                                         context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


@method_decorator(group_required(front_end_group), name='dispatch')
class ImageView(APIView):
    """
    API endpoint returning images
    """

    def get(self, request, id):
        interview = Interview.objects.get(id=id)
        img = interview.image
        response = HttpResponse(FileWrapper(img))
        return response


@method_decorator(group_required(front_end_group), name='dispatch')
class InterviewCountView(APIView):
    """
    API endpoint returning total number of interviews (displayed)
    """
    def get(self, request):
        queryset = Interview.objects.exclude(
            pull_quote__isnull=True).exclude(
            pull_quote__exact='').exclude(
            pull_quote__exact='0').count()
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
