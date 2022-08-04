# Copyright 2022 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.conf import settings
from django.contrib import admin
from django.urls import re_path, path, include
from django.views.generic import TemplateView
from interview_db.views import *
from . import views
# from rest_framework import routers, serializers, viewsets

app_name = "interview_db"

# start with an empty url array
urlpatterns = []

# add debug routes for developing error pages
if settings.DEBUG:
    urlpatterns += [
        re_path(
            r"^500$",
            TemplateView.as_view(template_name="500.html"),
            name="500_response",
        ),
        re_path(
            r"^404$",
            TemplateView.as_view(template_name="404.html"),
            name="404_response",
        ),
        re_path(
            r"^403$",
            TemplateView.as_view(template_name="403.html"),
            name="403_response",
        ),
    ]


urlpatterns += [
    re_path(r'^admin', admin.site.urls), 
    re_path(r"^(students|collections|about)$", DefaultPageView.as_view()),
    path('api/students/', InterviewListView.as_view(), name="student-list"),
    path('api/students/<int:pk>/', InterviewDetailView.as_view(), name="student-detail"),
    path('api/collections/', CollectionListView.as_view(), name="collection-list"),
    path('api/collections/<int:pk>/', CollectionDetailView.as_view(), name="collection-detail"),
    re_path(r"^.*$", TemplateView.as_view(template_name="vue.html"), name="home"),
]
