from django.shortcuts import render
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    """Home page for app djangos_ll"""
    return render(request, 'djangos_ll/index.html')

@login_required
def topics(request):
    """Views list them"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'djangos_ll/topics.html', context)

@login_required
def topic(request, topic_id):
    """Enter one topic and all them reads"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = { 'topic': topic, 'entries': entries }
    return render(request, 'djangos_ll/topic.html', context)

@login_required
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

@login_required
def new_entry(request, topic_id):
    """Added new entry by id"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        #add new empty form
        form = EntryForm()
    else:
        #Send data POST
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('djangos_ll:topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'djangos_ll/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit exists entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('djangos_ll:topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'djangos_ll/edit_entry.html', context)