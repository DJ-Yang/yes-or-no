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

def check_selection(request, topic_id):
  topic = get_object_or_404(Topic, pk=topic_id)
  user = request.user
  if user.is_authenticated:
    if topic.picks.filter(picker=user).exists():
      return redirect('topic:result', topic.id)
  else:
    return redirect('user:signin')
  return redirect('topic:select', topic.id)

@login_required(login_url='/auth/signin/')
def topic_select(request, topic_id):
  topic = get_object_or_404(Topic, pk=topic_id)

  return render(request, 'topic/select.html', {
    'topic': topic,
  })

@login_required(login_url='/auth/signin/')
@user_passes_test(lambda u: u.gender and u.age_range, login_url='/auth/add_info/')
def topic_result(request, topic_id):
  topic = get_object_or_404(Topic, pk=topic_id)
  picks = topic.picks.all()
  user = request.user

  if not picks.filter(picker=user):
    return redirect('topic:select', topic.id)
  else:
    pick = picks.filter(picker=user)
    user_selection = (topic.selection1_des) if selection == 0 else topic.selection2_des


  data = today_dailydata(topic)

  if selections:
    result = today_caculate_per(selections, topic)
  else:
    result = {}

  # data = simplejson.dumps(result)
  # print(data, result) 

  return render(request, 'topic/result.html', {
    'topic': topic,
    'result': result,
    'selections': selections,
    'data': data,
    'user_selection': user_selection,
  })

@login_required(login_url='/auth/signin/')
@user_passes_test(lambda u: u.gender and u.age_range, login_url='/auth/add_info/')
def set_selection(request):
  if request.method == 'POST':
    if request.is_ajax():
      select_type = int(request.POST.get('type'))
      topic_id = int(request.POST.get('topic_id'))
      topic = Topic.objects.get(pk=topic_id)
      user = request.user
      u_gender = 0 if (user.gender == 'male') else 1
      selection, is_selection = Selection.objects.get_or_create(topic=topic, selector=user, age_range=user.age_range, gender=u_gender)
      if is_selection:
        selection.select = select_type
        selection.updated_at = timezone.now()
        selection.save()
      else:
        if not selection.select == select_type:
          selection.select = select_type
          selection.updated_at = timezone.now()
          selection.save()
      result = {
        'status': True
      }
      return JsonResponse(result)


def user_request(request):
  return render(request, 'topic/request.html')