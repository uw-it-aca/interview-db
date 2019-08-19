from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from .models import Code, Interview
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    context_object_name = 'interview_list'
    login_url = '/admin/login/'
    def get_queryset(self):
        return Interview.objects.order_by('student')
        

class InterviewsView(LoginRequiredMixin, ListView):
    template_name = 'interviews.html'
    context_object_name = 'interview_list'
    login_url = '/admin/login/'
    def get_queryset(self):
        return Interview.objects.order_by('student')
        
class PeopleView(LoginRequiredMixin, ListView):
    template_name = 'people.html'
    context_object_name = 'interview_list'
    login_url = '/admin/login/'
    def get_queryset(self):
        return Interview.objects.order_by('student')

class TopicsView(LoginRequiredMixin, ListView):
    template_name = 'topics.html'
    context_object_name = 'code_list'
    login_url = '/admin/login/'
    def get_queryset(self):
        return Code.objects.order_by('topic','code')
        
def interview(request, interview_id):
    interview = get_object_or_404(Interview, pk=interview_id)
    return render(request, 'interview.html', {
        'interview': interview
        })

def code(request, code_id):
    code = get_object_or_404(Code, pk=code_id)
    return render(request, 'topic.html', {
        'code': code
        })