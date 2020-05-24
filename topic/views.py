from django.shortcuts import render, redirect
from .models import Topic, Selection
from django.http import HttpResponse, JsonResponse
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required
from user.models import User
# from django.utils import simplejson

def caculate_per(objects):
  total = objects.count()
  postive = objects.filter(select=0)
  negative = objects.filter(select=1)

  postive_value = postive.count()/total*100
  negative_value = negative.count()/total*100

  result = {
    'postive' : postive_value,
    'negative' : negative_value,
  }

  return result


def topic_list(request):
  topics = Topic.objects.all()

  return render(request, 'topic/list.html', {
    'topics': topics,
  })

def topic_select(request, topic_id):
  topic = Topic.objects.get(pk=topic_id)

  if request.user.is_authenticated:
    selection = topic.selection_set.filter(selector=request.user)
    if selection:
      return redirect('topic:result', topic.id)

  return render(request, 'topic/select.html', {
    'topic': topic,
  })

@login_required
def topic_result(request, topic_id):
  topic = Topic.objects.get(pk=topic_id)
  selections = topic.selection_set.all()

  result = caculate_per(selections)

  # data = simplejson.dumps(result)

  return render(request, 'topic/result.html', {
    'topic': topic,
    'result': result,
  })

@login_required
def set_selection(request):
  if request.method == 'POST':
    if request.is_ajax():
      select_type = int(request.POST.get('type'))
      topic_id = int(request.POST.get('topic_id'))
      topic = Topic.objects.get(pk=topic_id)
      user = request.user
      # age, gender 부분 유저 정보로 바꿔줘야함.
      selection, is_selection = Selection.objects.get_or_create(topic=topic, selector=user, age_range=1, gender=1)
      if is_selection:
        selection.select = select_type
        selection.save()
      else:
        selection.select = select_type
        selection.save()
      result = {
        'status': True
      }
      return JsonResponse(result)