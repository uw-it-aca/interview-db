# Copyright 2021 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.urls import re_path

from . import views

app_name = 'interview_db'
urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name="home"),
    re_path(r'interviews.html', views.InterviewsView.as_view(), name="interviews"),
    re_path(r'people.html', views.PeopleView.as_view(), name="people"),
    re_path(r'topics.html', views.TopicsView.as_view(), name="topics"),
    re_path(r'^interview/(?P<interview_id>\d+)/$',
        views.interview, name='interview'),
    re_path(r'^topic/(?P<code_id>\d+)/$',
        views.code, name='code'),
] 
