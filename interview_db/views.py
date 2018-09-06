from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Coding, SubCode, Story


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'code_list'
    def get_queryset(self):
        return Coding.objects.order_by('code')
        

class InterviewView(ListView):
    template_name = 'interview.html'
    context_object_name = 'story_list'
    def get_queryset(self):
        return Story.objects.order_by('interview','story_order_position')