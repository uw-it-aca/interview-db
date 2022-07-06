# Copyright 2022 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.conf import settings
from django.urls import re_path
from django.views.generic import TemplateView
from interview_db.views import DefaultPageView
from . import views

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
    ]

urlpatterns += [
    re_path(
        r"interviews.html", views.InterviewsView.as_view(), name="interviews"
    ),
    re_path(r"people.html", views.PeopleView.as_view(), name="people"),
    re_path(r"topics.html", views.TopicsView.as_view(), name="topics"),
    re_path(
        r"^interview/(?P<interview_id>\d+)/$",
        views.interview,
        name="interview",
    ),
    re_path(r"^topic/(?P<code_id>\d+)/$", views.code, name="code"),
    re_path(r"^(students|collections|about)$", DefaultPageView.as_view()),
    re_path(
        r"^$", TemplateView.as_view(template_name="vue.html"), name="home"
    ),
]
