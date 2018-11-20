from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from .models import Code, Interview


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'code_list'
    def get_queryset(self):
        return Code.objects.order_by('code')
        

class InterviewsView(ListView):
    template_name = 'interviews.html'
    context_object_name = 'interview_list'
    def get_queryset(self):
        return Interview.objects.order_by('student')
        
class PeopleView(ListView):
    template_name = 'people.html'
    context_object_name = 'interview_list'
    def get_queryset(self):
        return Interview.objects.order_by('student')

class TopicsView(ListView):
    template_name = 'topics.html'
    context_object_name = 'code_list'
    def get_queryset(self):
        return Code.objects.order_by('code')
        
def interview(request, interview_id):
    interview = get_object_or_404(Interview, pk=interview_id)
    return render(request, 'interview.html', {
        'interview': interview
        })