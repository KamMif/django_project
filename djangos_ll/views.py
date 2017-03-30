from django.shortcuts import render
from .models import Topic

def index(request):
    """Home page for app djangos_ll"""
    return render(request, 'djangos_ll/index.html')

def topics(request):
    """Views list them"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'djangos_ll/topics.html', context)

def topic(request, topic_id):
    """Enter one topic and all them reads"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = { 'topic': topic, 'entries': entries }
    return render(request, 'djangos_ll/topic.html', context)
