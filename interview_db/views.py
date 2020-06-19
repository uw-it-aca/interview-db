from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from .models import Code, Interview
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required(), name='dispatch')
class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'interview_list'
    def get_queryset(self):
        return Interview.objects.order_by('student')


@method_decorator(login_required(), name='dispatch')
class InterviewsView(ListView):
    template_name = 'interviews.html'
    context_object_name = 'interview_list'
    def get_queryset(self):
        return Interview.objects.order_by('student')


@method_decorator(login_required(), name='dispatch')
class PeopleView(ListView):
    template_name = 'people.html'
    context_object_name = 'interview_list'
    def get_queryset(self):
        return Interview.objects.order_by('student')


@method_decorator(login_required(), name='dispatch')
class TopicsView(ListView):
    template_name = 'topics.html'
    context_object_name = 'code_list'
    def get_queryset(self):
        return Code.objects.order_by('topic','code')


@login_required()
def interview(request, interview_id):
    interview = get_object_or_404(Interview, pk=interview_id)
    return render(request, 'interview.html', {
        'interview': interview
        })


@login_required()
def code(request, code_id):
    code = get_object_or_404(Code, pk=code_id)
    return render(request, 'topic.html', {
        'code': code
        })