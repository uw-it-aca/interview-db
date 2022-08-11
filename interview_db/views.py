# Copyright 2022 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from uw_saml.decorators import group_required
from django.views.decorators.csrf import csrf_exemt
from rest_framework.parsers import JSONParser
from rest_framework import permissions, generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from .serializers import *
from .models import Code, Interview

admin_group = settings.INTERVIEW_DB_AUTHZ_GROUPS['admin']
front_end_group = settings.INTERVIEW_DB_AUTHZ_GROUPS['front-end']


class PageView(TemplateView):
    template_name = "vue.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def render_to_response(self, context, **response_kwargs):
        response = super(PageView, self).render_to_response(
            context, **response_kwargs)
        return response


class DefaultPageView(PageView):
    template_name = "vue.html"


class InterviewListView(APIView):
    """
    API endpoint returning list of interviews
    """

    def get(self, request):
        queryset = Interview.objects.all().order_by('-date')
        serializer = InterviewSerializer(queryset, many=True,
                                         context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class InterviewDetailView(APIView):
    """
    API endpoint returning single interview, made up of its matching stories
    """

    def get(self, request, id):
        queryset = Story.objects.filter(interview__id=id)
        serializer = StorySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CollectionListView(APIView):
    """
    API endpoint returning list of collections
    """

    def get(self, request):
        queryset = Collection.objects.all()
        serializer = CollectionSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CollectionDetailView(APIView):
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


class MajorListView(APIView):
    """
    API endpoint returning all added majors
    """

    def get(self, request):
        queryset = Major.objects.all()
        serializer = MajorSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StudentTypeListView(APIView):
    """
    API endpoint returning all added majors
    """

    def get(self, request):
        queryset = StudentType.objects.all()
        serializer = StudentTypeSerializer(queryset, many=True)
        return Response(serializer.data)


class StoryListView(APIView):
    """
    API endpoint returning all stories
    """

    def get(self, request):
        queryset = Story.objects.all()
        serializer = StorySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
