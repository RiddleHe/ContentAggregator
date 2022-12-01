from django.urls import re_path, path
from . import views

app_name='aggregators'

urlpatterns = [

    re_path(r'^$', views.index, name="index"),
    re_path(r'^topics/(?P<topic_name>[-\w]+)/$', views.topic, name="topic"),
    re_path(r'^add_rss/$', views.add_rss, name="add_rss"),
]