from django.shortcuts import render
from .models import Topic, Selection

# Create your views here.

def topic_list(request):
  topics = Topic.objects.all()

  return render(request, 'topic/list.html', {
    'topics': topics,
  })

def topic_detail(request, topic_id):
  topic = Topic.objects.get(pk=topic_id)

  return render(request, 'topic/topic.html', {
    'topic': topic,
  })