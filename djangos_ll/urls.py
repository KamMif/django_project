"""Schema URL for djangos_ll"""
from django.conf.urls import url
from . import views

urlpatterns = [
    #Home directory
    url(r'^$', views.index, name='index'),
    #views all thems
    url(r'^topics/$', views.topics, name='topics'),
    #Page for one them
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    #Page for add new Topic
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    #Page for added new Entry
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    #Page for edit Entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]