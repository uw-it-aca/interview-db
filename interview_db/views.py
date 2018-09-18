from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Code, Interview


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'code_list'
    def get_queryset(self):
        return Code.objects.order_by('code')
        

class InterviewView(ListView):
    template_name = 'interview.html'
    context_object_name = 'interview_list'
    def get_queryset(self):
        return Interview.objects.order_by('student')