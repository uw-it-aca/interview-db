# Copyright 2022 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.conf import settings
from django.contrib import admin
from django.urls import re_path, path
from django.views.generic import TemplateView
from django.conf.urls.static import static
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
    re_path(r"^(students|collections|about)$", DefaultPageView.as_view()),
    path('api/students/', InterviewListView.as_view(), name="student-list"),
    path('api/students/<int:id>/', InterviewDetailView.as_view(),
         name="student-detail"),
    path('api/collections/', CollectionListView.as_view(),
         name="collection-list"),
    path('api/collections/<str:topic>/', CollectionDetailView.as_view(),
         name="collection-detail"),
    path('api/majors/', MajorListView.as_view(), name="major-list"),
    path('api/types/', StudentTypeListView.as_view(), name="type-list"),
    path('api/random/', RandomStudentsView.as_view(), name="random-students"),
    path('api/recent/', RecentStudentsView.as_view(), name="recent-students"),
    path('api/codes/', CodesListView.as_view()),
    re_path(r"^.*$", TemplateView.as_view(
        template_name="vue.html"),
        name="home"),
]
