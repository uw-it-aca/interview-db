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
        response = super(PageView, self).render_to_response(context, **response_kwargs)
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
    API endpoint returning single interview
    """

    def get(self, request, interview_id):
        queryset = get_object_or_404(Interview.objects.all(), pk=interview_id)
        serializer = InterviewSerializer(queryset, many=False)
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

    def get(self, request, code):
        queryset = Story.objects.filter(code=code).get()
        serializer = StorySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# @method_decorator(group_required(front_end_group), name='dispatch')
# class IndexView(ListView):
#     template_name = 'index.html'
#     context_object_name = 'interview_list'
#     def get_queryset(self):
#         return Interview.objects.order_by('student')
#
#
# @method_decorator(group_required(front_end_group), name='dispatch')
# class InterviewsView(ListView):
#     template_name = 'interviews.html'
#     context_object_name = 'interview_list'
#     def get_queryset(self):
#         return Interview.objects.order_by('student')
#
#
# @method_decorator(group_required(front_end_group), name='dispatch')
# class PeopleView(ListView):
#     template_name = 'people.html'
#     context_object_name = 'interview_list'
#     def get_queryset(self):
#         return Interview.objects.order_by('student')
#
#
# @method_decorator(group_required(front_end_group), name='dispatch')
# class TopicsView(ListView):
#     template_name = 'collections.html'
#     context_object_name = 'code_list'
#     def get_queryset(self):
#         return Code.objects.order_by('topic', 'code')
#
#
# @group_required(front_end_group)
# def interview(request, interview_id):
#     interview = get_object_or_404(Interview, pk=interview_id)
#     return render(request, 'interview.html', {
#         'interview': interview
#         })
#
#
# @group_required(front_end_group)
# def code(request, code_id):
#     code = get_object_or_404(Code, pk=code_id)
#     return render(request, 'topic.html', {
#         'code': code
#         })