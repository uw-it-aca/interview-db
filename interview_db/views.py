from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Coding


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'code_list'
    def get_queryset(self):
        return Coding.objects.order_by('code')