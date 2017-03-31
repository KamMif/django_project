from django.shortcuts import render
from .models import Topic
from .forms import TopicForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

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

def new_topic(request):
    """Add new Topic"""
    if request.method != 'POST':
        #Data not sending; create empty form
        form = TopicForm()
    else:
        #Data send
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('djangos_ll:topics'))
    context = {'form': form}
    return render(request, 'djangos_ll/new_topic.html', context)