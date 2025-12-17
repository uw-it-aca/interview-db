# copyright 2026 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.conf import settings
from django.contrib import admin
from django.urls import re_path, path
from django.views.generic import TemplateView
from interview_db.views import *

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
    path('students', DefaultPageView.as_view(), name="students"),
    path('collections', DefaultPageView.as_view(), name="collections"),
    path('about', DefaultPageView.as_view(), name="about"),
    path('api/students/', InterviewListView.as_view(),
         name="student-list"),
    path('api/students/<int:id>/', SingleInterviewView.as_view(),
         name="student-detail"),
    path('api/students/<int:id>/image/', ImageView.as_view(),
         name="student-image"),
    path('api/students/<int:id>/topics/', InterviewTopicsView.as_view(),
         name="interview-topics"),
    path('api/collections/', CollectionListView.as_view(),
         name="collection-list"),
    path('api/collections/<int:id>/info/',
         CollectionInfoView.as_view(),
         name="collection-info",),
    path('api/collections/<int:id>/',
         CollectionStoryView.as_view(),
         name="collection-stories",),
    path('api/majors/', MajorListView.as_view(), name="major-list"),
    path('api/random/', RandomStudentsView.as_view(), name="random-students"),
    path('api/students/count/', InterviewCountView.as_view(),
         name="interview-count"),
    path('api/stories/count/', StoryCountView.as_view(), name="story-count"),
    re_path(r"^.*$", DefaultPageView.as_view(), name="home"),
]
