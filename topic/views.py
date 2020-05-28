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

def convert(topic_list): 
    return tuple(i[0] for i in topic_list) 

# 핫 토픽 설정 부분
# updated_at 필드를 추가해서 기존에 설문에 참여했던 사람이 값을 변경했을 경우도 값에 포함될 수 있게 함.
# 매일 오전 00시 00분에 실행되게 데코레이터 사용
def set_hot_topic():
  yesterday = datetime.date.today() - datetime.timedelta(days=1)
  today_selections = Selection.objects.filter(updated_at__date=yesterday)

  topic_list = {
  }
  hot_topic_list = []

  for selection in today_selections:
    if selection.topic.id in topic_list:
      topic_list[selection.topic.id] += 1
    else:
      topic_list[selection.topic.id] = 1

  topic_list = sorted(topic_list.items(), key=(lambda x : x[0]), reverse=True)

  for topic in topic_list:
    if len(hot_topic_list) >= 3:
      if hot_topic_list[2][1] < topic[1]:
        hot_topic_list[2] = topic
    else:
      hot_topic_list.append(topic)
    hot_topic_list = sorted(hot_topic_list, key=(lambda x : x[1]), reverse=True)

  hot_topic_id = convert(hot_topic_list)

  test = Topic.objects.filter(hot_topic=True).update(hot_topic=False)

  Topic.objects.filter(id__in=hot_topic_id).update(hot_topic=True)

def topic_list(request):
  topics = Topic.objects.all()

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


def user_request(request):
  return render(request, 'topic/request.html')

def notice(request):
  return render(request, 'topic/notice.html')