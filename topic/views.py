from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic, Selection, Pick, DailyPick
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from user.models import User
from django.utils import timezone
import datetime

def convert(topic_list): 
    return tuple(i[0] for i in topic_list)

# 데일리 데이터 저장 부분
def store_daily_pick():
  topics = Topic.objects.all()

  for topic in topics:
    picks = Topic.picks.all()

    todaypick = DailyPick()
    todaypick.pick1 = picks.filter(selection=1).count()
    todaypick.pick2 = picks.filter(selection=2).count()
    todaypick.pick3 = picks.filter(selection=3).count()
    todaypick.pick4 = picks.filter(selection=4).count()
    todaypick.save()

# 핫 토픽 설정 부분
# updated_at 필드를 추가해서 기존에 설문에 참여했던 사람이 값을 변경했을 경우도 값에 포함될 수 있게 함.
# 매일 오전 00시 00분에 실행되게 데코레이터 사용
def set_hot_topic():
  yesterday = datetime.date.today() - datetime.timedelta(days=1)
  today_picks = Pick.objects.filter(updated_at__date=yesterday)

  topic_list = {
  }
  hot_topic_list = []

  for pick in today_picks:
    if pick.topic.id in topic_list:
      topic_list[pick.topic.id] += 1
    else:
      topic_list[pcik.topic.id] = 1

  topic_list = sorted(topic_list.items(), key=(lambda x : x[0]), reverse=True)

  for topic in topic_list:
    if len(hot_topic_list) >= 3:
      if hot_topic_list[2][1] < topic[1]:
        hot_topic_list[2] = topic
    else:
      hot_topic_list.append(topic)
    hot_topic_list = sorted(hot_topic_list, key=(lambda x : x[1]), reverse=True)

  hot_topic_id = convert(hot_topic_list)

  Topic.objects.filter(hot_topic=True).update(hot_topic=False)

  Topic.objects.filter(id__in=hot_topic_id).update(hot_topic=True)

# result page에 접속할때마다 현재까지 결과 값을 확인하는 과정
def set_data(objects):
  selections = [x for x in range(1, objects.selection_amount+1)]
  ages = [10, 20, 30, 40, 50, 60]
  genders = [0, 1]

  result = {}

  for selection in selections:
    picks = objects.picks.filter(selection=selection)
    result["selection_" + str(selection)] = picks.count()
    for age in ages:
      result["selection_" + str(selection) + "_" + str(age)] = picks.filter(selection=selection, age_range=age).count()
      for gender in genders:
        result["selection_" + str(selection) + "_" + str(gender)] = picks.filter(selection=selection, gender=gender).count()
        result["selection_" + str(selection) + "_" + str(age) + "_" + str(gender)] = picks.filter(selection=selection, age_range=age, gender=gender).count()
  
  return result

def topic_list(request):
  topics = Topic.objects.all().order_by('-created_at')
  hot_topics = Topic.objects.filter(hot_topic=True)

  return render(request, 'topic/list.html', {
    'topics' : topics,
    'hot_topics' : hot_topics,
  })

@login_required(login_url='/auth/signin/')
@user_passes_test(lambda u: u.gender and u.age_range, login_url='/auth/add_info/')
def check_selection(request, topic_id):
  topic = get_object_or_404(Topic, pk=topic_id)

  print(request.user)

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

    if not request.POST.get('pick'):
      return redirect('topic:select', topic.id)
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
  pick = topic.picks.get(author=request.user)
  data = set_data(topic)
  
  return render(request, 'topic/result.html', {
    'topic' : topic,
    'pick' : pick,
    'data' : data,
  })

def user_request(request):
  return render(request, 'topic/request.html')