# Copyright 2023 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0


from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView

from uw_saml.decorators import group_required

from .models import Code, Interview

admin_group = settings.INTERVIEW_DB_AUTHZ_GROUPS['admin']
front_end_group = settings.INTERVIEW_DB_AUTHZ_GROUPS['front-end']

@method_decorator(group_required(front_end_group), name='dispatch')
class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'interview_list'
    def get_queryset(self):
        return Interview.objects.order_by('student')


@method_decorator(group_required(front_end_group), name='dispatch')
class InterviewsView(ListView):
    template_name = 'interviews.html'
    context_object_name = 'interview_list'
    def get_queryset(self):
        return Interview.objects.order_by('student')


@method_decorator(group_required(front_end_group), name='dispatch')
class PeopleView(ListView):
    template_name = 'people.html'
    context_object_name = 'interview_list'
    def get_queryset(self):
        return Interview.objects.order_by('student')


@method_decorator(group_required(front_end_group), name='dispatch')
class TopicsView(ListView):
    template_name = 'topics.html'
    context_object_name = 'code_list'
    def get_queryset(self):
        return Code.objects.order_by('topic','code')


@group_required(front_end_group)
def interview(request, interview_id):
    interview = get_object_or_404(Interview, pk=interview_id)
    return render(request, 'interview.html', {
        'interview': interview
        })


@group_required(front_end_group)
def code(request, code_id):
    code = get_object_or_404(Code, pk=code_id)
    return render(request, 'topic.html', {
        'code': code
        })