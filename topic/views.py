from django.shortcuts import render
from .models import Topic, Selection

# Create your views here.
def home(request):
  return render(request, 'base.html', {
  })

def topic_list(request):
  topics = Topic.objects.all()

  return render(request, 'topic/list.html', {
    'topics': topics,
  })