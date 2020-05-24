from django.shortcuts import render, redirect
from .models import Topic, Selection
from django.http import HttpResponse, JsonResponse
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required
from user.models import User
from django.utils import timezone
import datetime
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

# 핫 토픽 설정 부분
# updated_at 필드를 추가해서 기존에 설문에 참여했던 사람이 값을 변경했을 경우도 값에 포함될 수 있게 함.
def set_hot_topic():
  start_day = timezone.now() - timezone.timedelta(days=2)
  end_day = timezone.now() - timezone.timedelta(days=1)
  selections = Selection.objects.all()
  today_selections = selections.filter(updated_at__gte=start_day, updated_at__lte=end_day)

  for selection in today_selections:
    topic_id = selection.topic.id

def topic_list(request):
  topics = Topic.objects.all()

  set_hot_topic()

  return render(request, 'topic/list.html', {
    'topics': topics,
  })

def topic_select(request, topic_id):
  topic = Topic.objects.get(pk=topic_id)

  # result.html 에 수정 버튼이 생기면 주석을 풀어줄 것
  # if request.user.is_authenticated:
  #   selection = topic.selection_set.filter(selector=request.user)
  #   if selection:
  #     return redirect('topic:result', topic.id)

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