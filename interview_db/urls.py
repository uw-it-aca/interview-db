from django.conf.urls import url
from . import views

app_name = 'interview_db'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="home"),
    url(r'interviews.html', views.InterviewView.as_view(), name="interviews"),
    url(r'people.html', views.PeopleView.as_view(), name="people"),
] 
