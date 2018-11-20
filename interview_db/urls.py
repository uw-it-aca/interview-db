from django.conf.urls import url
from . import views

app_name = 'interview_db'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="home"),
    url(r'interviews.html', views.InterviewsView.as_view(), name="interviews"),
    url(r'people.html', views.PeopleView.as_view(), name="people"),
    url(r'topics.html', views.TopicsView.as_view(), name="topics"),
    url(r'^interview/(?P<interview_id>\d+)/$',
        views.interview, name='interview'),
    url(r'^topic/(?P<code_id>\d+)/$',
        views.code, name='code'),
] 
