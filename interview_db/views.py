# Copyright 2022 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from uw_saml.decorators import group_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import permissions, generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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
        queryset = Interview.objects.all().order_by('date')
        serializer = InterviewSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class InterviewDetailView(APIView):
    """
    API endpoint returning single interview, made up of its matching stories
    """

    def get(self, request, interview_id):
        queryset = Story.objects.filter(interview=interview_id)
        serializer = StorySerializer(queryset, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CollectionListView(APIView):
    """
    API endpoint returning list of collections
    """

    def get(self, request):
        queryset = Code.objects.all()
        serializer = CodeSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CollectionDetailView(APIView):
    """
    API endpoint returning single collection
    """

    def get(self, request, codes, subcodes):
        # queryset = Story.objects.filter(code_in=codes)
        # queryset += Story.objects.filter(subcode_in=subcodes)
        queryset = Coding.objects.filter(code_in=codes).values_list(
            'story', flat=True)
        queryset += Coding.objects.filter(code_in=subcodes).values_list(
            'story', flat=True)
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
