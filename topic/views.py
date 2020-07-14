from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic, Selection
from django.http import HttpResponse, JsonResponse
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required, user_passes_test
from user.models import User
from django.utils import timezone
import datetime
import json
# from django.utils import simplejson

# def convert(topic_list): 
#     return tuple(i[0] for i in topic_list) 

def topic_list(request):
  topics = Topic.objects.all().order_by('-created_at')
  hot = Topic.objects.filter(hot_topic=True)

  return render(request, 'topic/list.html', {
    'topics': topics,
    'hot':hot,
  })

def user_request(request):
  return render(request, 'topic/request.html')