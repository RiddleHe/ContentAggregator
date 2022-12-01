from django.urls import re_path, path
from . import views

app_name='aggregators'

urlpatterns = [

    re_path(r'^$', views.index, name="index"),
    re_path(r'^topics/(?P<topic_name>[-\w]+)/$', views.topic, name="topic"),
    # for the adding rss page
    re_path(r'^add_rss/$', views.add_rss, name="add_rss"),
    # for refresh the page to update feedparser
    re_path(r'^update_rss/$', views.update_rss, name="update_rss"),
]