from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic, Selection, Pick
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

# daily data
def set_data(objects):
  selections = [x for x in range(1, objects.selection_amount+1)]
  ages = [10, 20, 30, 40, 50, 60]
  genders = [0, 1]

  return_data = {}

  for selection in selections:
    picks = objects.picks.filter(selection=selection)
    return_data["selection_" + str(selection)] = picks.count()
    for age in ages:
      return_data["selection_" + str(selection) + "_" + str(age)] = picks.filter(selection=selection, age_range=age).count()
      for gender in genders:
        return_data["selection_" + str(selection) + "_" + str(gender)] = picks.filter(selection=selection, gender=gender).count()
        return_data["selection_" + str(selection) + "_" + str(age) + "_" + str(gender)] = picks.filter(selection=selection, age_range=age, gender=gender).count()
  
  return return_data

def topic_list(request):
  topics = Topic.objects.all().order_by('-created_at')
  hot_topics = Topic.objects.filter(hot_topic=True)
  test = Topic.objects.get(pk=1)
  set_data(test)

  return render(request, 'topic/list.html', {
    'topics' : topics,
    'hot_topics' : hot_topics,
  })

@login_required(login_url='/auth/signin/')
@user_passes_test(lambda u: u.gender and u.age_range, login_url='/auth/add_info/')
def check_selection(request, topic_id):
  topic = get_object_or_404(Topic, pk=topic_id)

  if topic.picks.filter(author=request.user).exists():
    return redirect('topic:result', topic.id)
  else:
    return render(request, 'topic/select.html', {
      'topic' : topic,
    })

@login_required(login_url='/auth/signin/')
@user_passes_test(lambda u: u.gender and u.age_range, login_url='/auth/add_info/')
def topic_select(request, topic_id):
  topic = get_object_or_404(Topic, pk=topic_id)

  if request.method == 'POST':
    u_gender = 0 if (request.user.gender == 'male') else 1
    pick, created = Pick.objects.get_or_create(
      author=request.user,
      topic=topic,
      age_range=request.user.age_range,
      gender=u_gender
    )
    if created:
        pick.selection = request.POST.get('pick')
        pick.updated_at = timezone.now()
        pick.save()
    else:
      if not pick.selection == request.POST.get('pick'):
        pick.selection = request.POST.get('pick')
        pick.updated_at = timezone.now()
        pick.save()
    return redirect('topic:result', topic.id)


  return render(request, 'topic/select.html', {
    'topic' : topic,
  })


@login_required(login_url='/auth/signin/')
def topic_result(request, topic_id):
  topic = get_object_or_404(Topic, pk=topic_id)
  pick = topic.picks.filter(author=request.user)
  
  return render(request, 'topic/result.html', {
    'topic' : topic,
    'pick' : pick,
  })

def user_request(request):
  return render(request, 'topic/request.html')