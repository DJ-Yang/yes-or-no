from django.shortcuts import render, redirect
from .models import Topic, Selection, DailyData
from django.http import HttpResponse, JsonResponse
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required, user_passes_test
from user.models import User
from django.utils import timezone
import datetime
# from django.utils import simplejson

def convert(topic_list): 
    return tuple(i[0] for i in topic_list) 

def create_daily_data():
  topics = Topic.objects.all()
  
  for topic in topics:
    selections = topic.selection_set.all()
    total = selections.count()
    postive = selections.filter(select=0)
    negative = selections.filter(select=1)
    postive_male = postive.filter(gender=0)
    postive_female = postive.filter(gender=1)
    negative_male = negative.filter(gender=0)
    negative_female = negative.filter(gender=1)
    postive_10age = postive.filter(age_range=10)
    postive_10age_male = postive_10age.filter(gender=0)
    postive_10age_female = postive_10age.filter(gender=1)
    postive_20age = postive.filter(age_range=20)
    postive_20age_male = postive_20age.filter(gender=0)
    postive_20age_female = postive_20age.filter(gender=1)
    postive_30age = postive.filter(age_range=30)
    postive_30age_male = postive_30age.filter(gender=0)
    postive_30age_female = postive_30age.filter(gender=1)
    postive_40age = postive.filter(age_range=40)
    postive_40age_male = postive_40age.filter(gender=0)
    postive_40age_female = postive_40age.filter(gender=1)
    postive_50age = postive.filter(age_range=50)
    postive_50age_male = postive_50age.filter(gender=0)
    postive_50age_female = postive_50age.filter(gender=1)
    postive_60age = postive.filter(age_range=60)
    postive_60age_male = postive_60age.filter(gender=0)
    postive_60age_female = postive_60age.filter(gender=1)
    negative_10age = negative.filter(age_range=10)
    negative_10age_male = negative_10age.filter(gender=0)
    negative_10age_female = negative_10age.filter(gender=1)
    negative_20age = negative.filter(age_range=20)
    negative_20age_male = negative_20age.filter(gender=0)
    negative_20age_female = negative_20age.filter(gender=1)
    negative_30age = negative.filter(age_range=30)
    negative_30age_male = negative_30age.filter(gender=0)
    negative_30age_female = negative_30age.filter(gender=1)
    negative_40age = negative.filter(age_range=40)
    negative_40age_male = negative_40age.filter(gender=0)
    negative_40age_female = negative_40age.filter(gender=1)
    negative_50age = negative.filter(age_range=50)
    negative_50age_male = negative_50age.filter(gender=0)
    negative_50age_female = negative_50age.filter(gender=1)
    negative_60age = negative.filter(age_range=60)
    negative_60age_male = negative_60age.filter(gender=0)
    negative_60age_female = negative_60age.filter(gender=1)


    data = DailyData()
    data.topic = topic
    data.postive_count = postive.count()
    data.negative_count = negative.count()
    data.postive_male_count = postive_male.count()
    data.postive_female_count = postive_female.count()
    data.negative_male_count = negative_male.count()
    data.negative_female_count = negative_female.count()
    data.postive_10age_count = postive_10age.count()
    data.postive_10age_male_count = postive_10age_male.count()
    data.postive_10age_female_count = postive_10age_female.count()
    data.postive_20age_count = postive_20age.count()
    data.postive_20age_male_count = postive_20age_male.count()
    data.postive_20age_female_count = postive_20age_female.count()
    data.postive_30age_count = postive_30age.count()
    data.postive_30age_male_count = postive_30age_male.count()
    data.postive_30age_female_count = postive_30age_female.count()
    data.postive_40age_count = postive_40age.count()
    data.postive_40age_male_count = postive_40age_male.count()
    data.postive_40age_female_count = postive_40age_female.count()
    data.postive_50age_count = postive_50age.count()
    data.postive_50age_male_count = postive_50age_male.count()
    data.postive_50age_female_count = postive_50age_female.count()
    data.postive_60age_count = postive_60age.count()
    data.postive_60age_male_count = postive_60age_male.count()
    data.postive_60age_female_count = postive_60age_female.count()
    data.negative_10age_count = negative_10age.count()
    data.negative_10age_male_count = negative_10age_male.count()
    data.negative_10age_female_count = negative_10age_female.count()
    data.negative_20age_count = negative_20age.count()
    data.negative_20age_male_count = negative_20age_male.count()
    data.negative_20age_female_count = negative_20age_female.count()
    data.negative_30age_count = negative_30age.count()
    data.negative_30age_male_count = negative_30age_male.count()
    data.negative_30age_female_count = negative_30age_female.count()
    data.negative_40age_count = negative_40age.count()
    data.negative_40age_male_count = negative_40age_male.count()
    data.negative_40age_female_count = negative_40age_female.count()
    data.negative_50age_count = negative_50age.count()
    data.negative_50age_male_count = negative_50age_male.count()
    data.negative_50age_female_count = negative_50age_female.count()
    data.negative_60age_count = negative_60age.count()
    data.negative_60age_male_count = negative_60age_male.count()
    data.negative_60age_female_count = negative_60age_female.count()

    data.save()

def today_caculate_per(objects, topic):
  total = objects.count()
  postive = objects.filter(select=0)
  negative = objects.filter(select=1)
  male = objects.filter(gender=0)
  female = objects.filter(gender=1)
  age10 = objects.filter(age_range=10)
  age20 = objects.filter(age_range=20)
  age30 = objects.filter(age_range=30)
  age40 = objects.filter(age_range=40)
  age50 = objects.filter(age_range=50)
  age60 = objects.filter(age_range=60)
  postive_male = postive.filter(gender=0)
  postive_female = postive.filter(gender=1)
  negative_male = negative.filter(gender=0)
  negative_female = negative.filter(gender=1)
  postive_10age = postive.filter(age_range=10)
  postive_10age_male = postive_10age.filter(gender=0)
  postive_10age_female = postive_10age.filter(gender=1)
  postive_20age = postive.filter(age_range=20)
  postive_20age_male = postive_20age.filter(gender=0)
  postive_20age_female = postive_20age.filter(gender=1)
  postive_30age = postive.filter(age_range=30)
  postive_30age_male = postive_30age.filter(gender=0)
  postive_30age_female = postive_30age.filter(gender=1)
  postive_40age = postive.filter(age_range=40)
  postive_40age_male = postive_40age.filter(gender=0)
  postive_40age_female = postive_40age.filter(gender=1)
  postive_50age = postive.filter(age_range=50)
  postive_50age_male = postive_50age.filter(gender=0)
  postive_50age_female = postive_50age.filter(gender=1)
  postive_60age = postive.filter(age_range=60)
  postive_60age_male = postive_60age.filter(gender=0)
  postive_60age_female = postive_60age.filter(gender=1)
  negative_10age = negative.filter(age_range=10)
  negative_10age_male = negative_10age.filter(gender=0)
  negative_10age_female = negative_10age.filter(gender=1)
  negative_20age = negative.filter(age_range=20)
  negative_20age_male = negative_20age.filter(gender=0)
  negative_20age_female = negative_20age.filter(gender=1)
  negative_30age = negative.filter(age_range=30)
  negative_30age_male = negative_30age.filter(gender=0)
  negative_30age_female = negative_30age.filter(gender=1)
  negative_40age = negative.filter(age_range=40)
  negative_40age_male = negative_40age.filter(gender=0)
  negative_40age_female = negative_40age.filter(gender=1)
  negative_50age = negative.filter(age_range=50)
  negative_50age_male = negative_50age.filter(gender=0)
  negative_50age_female = negative_50age.filter(gender=1)
  negative_60age = negative.filter(age_range=60)
  negative_60age_male = negative_60age.filter(gender=0)
  negative_60age_female = negative_60age.filter(gender=1)

  # 일일 투표 데이터 비율
  postive_value = (postive.count()/total*100) if not(total == 0) else 0
  negative_value = (negative.count()/total*100) if not(total == 0) else 0

  # 전체 데이터
  postive_10age_male_value = (postive_10age_male.count()/total*100) if not(total == 0) else 0
  postive_10age_female_value = (postive_10age_female.count()/total*100) if not(total == 0) else 0
  negative_10age_male_value = (negative_10age_male.count()/total*100) if not(total == 0) else 0
  negative_10age_female_value = (negative_10age_female.count()/total*100) if not(total == 0) else 0
  postive_20age_male_value = (postive_20age_male.count()/total*100) if not(total == 0) else 0
  postive_20age_female_value = (postive_20age_female.count()/total*100) if not(total == 0) else 0
  negative_20age_male_value = (negative_20age_male.count()/total*100) if not(total == 0) else 0
  negative_20age_female_value = (negative_20age_female.count()/total*100) if not(total == 0) else 0
  postive_30age_male_value = (postive_30age_male.count()/total*100) if not(total == 0) else 0
  postive_30age_female_value = (postive_30age_female.count()/total*100) if not(total == 0) else 0
  negative_30age_male_value = (negative_30age_male.count()/total*100) if not(total == 0) else 0
  negative_30age_female_value = (negative_30age_female.count()/total*100) if not(total == 0) else 0
  postive_40age_male_value = (postive_40age_male.count()/total*100) if not(total == 0) else 0
  postive_40age_female_value = (postive_40age_female.count()/total*100) if not(total == 0) else 0
  negative_40age_male_value = (negative_40age_male.count()/total*100) if not(total == 0) else 0
  negative_40age_female_value = (negative_40age_female.count()/total*100) if not(total == 0) else 0
  postive_50age_male_value = (postive_50age_male.count()/total*100) if not(total == 0) else 0
  postive_50age_female_value = (postive_50age_female.count()/total*100) if not(total == 0) else 0
  negative_50age_male_value = (negative_50age_male.count()/total*100) if not(total == 0) else 0
  negative_50age_female_value = (negative_50age_female.count()/total*100) if not(total == 0) else 0
  postive_60age_male_value = (postive_60age_male.count()/total*100) if not(total == 0) else 0
  postive_60age_female_value = (postive_60age_female.count()/total*100) if not(total == 0) else 0
  negative_60age_male_value = (negative_60age_male.count()/total*100) if not(total == 0) else 0
  negative_60age_female_value = (negative_60age_female.count()/total*100) if not(total == 0) else 0
  
  # 성별 데이터
  postive_male_value = (postive_male.count()/male.count()*100) if not (male.count() == 0) else 0
  postive_female_value = (postive_female.count()/female.count()*100) if not (female.count() == 0) else 0
  negative_male_value = (negative_male.count()/male.count()*100) if not (male.count() == 0) else 0
  negative_female_value = (negative_female.count()/female.count()*100) if not (female.count() == 0) else 0

  # 연령별 데이터
  postive_10age_value = (postive_10age.count()/age10.count()*100) if not (age10.count() == 0) else 0
  postive_20age_value = (postive_20age.count()/age20.count()*100) if not (age20.count() == 0) else 0
  postive_30age_value = (postive_30age.count()/age30.count()*100) if not (age30.count() == 0) else 0
  postive_40age_value = (postive_40age.count()/age40.count()*100) if not (age40.count() == 0) else 0
  postive_50age_value = (postive_50age.count()/age50.count()*100) if not (age50.count() == 0) else 0
  postive_60age_value = (postive_60age.count()/age60.count()*100) if not (age60.count() == 0) else 0
  negative_10age_value = (negative_10age.count()/age10.count()*100) if not (age10.count() == 0) else 0
  negative_20age_value = (negative_20age.count()/age20.count()*100) if not (age20.count() == 0) else 0
  negative_30age_value = (negative_30age.count()/age30.count()*100) if not (age30.count() == 0) else 0
  negative_40age_value = (negative_40age.count()/age40.count()*100) if not (age40.count() == 0) else 0
  negative_50age_value = (negative_50age.count()/age50.count()*100) if not (age50.count() == 0) else 0
  negative_60age_value = (negative_60age.count()/age60.count()*100) if not (age60.count() == 0) else 0
  
  # 주별, 월별, 연별(보류) 데이터 다른 함수로 만들기

  result = {
    'postive' : postive_value,
    'negative' : negative_value,
    'postive_male' : postive_male_value,
    'postive_female' : postive_female_value,
    'negetive_male' : negative_male_value,
    'negative_female' : negative_female_value,
    'postive_10age' : postive_10age_value,
    'postive_20age' : postive_20age_value,
    'postive_30age' : postive_30age_value,
    'postive_40age' : postive_40age_value,
    'postive_50age' : postive_50age_value,
    'postive_60age' : postive_60age_value,
    'negative_10age' : negative_10age_value,
    'negative_20age' : negative_20age_value,
    'negative_30age' : negative_30age_value,
    'negative_40age' : negative_40age_value,
    'negative_50age' : negative_50age_value,
    'negative_60age' : negative_60age_value,
    'postive_10age_male' : postive_10age_male_value,
    'postive_10age_female' : postive_10age_female_value,
    'negative_10age_male' : negative_10age_male_value,
    'negative_10age_female' : negative_10age_female_value,
    'postive_20age_male' : postive_20age_male_value,
    'postive_20age_female' : postive_20age_female_value,
    'negative_20age_male' : negative_20age_male_value,
    'negative_20age_female' : negative_20age_female_value,
    'postive_30age_male' : postive_30age_male_value,
    'postive_30age_female' : postive_30age_female_value,
    'negative_30age_male' : negative_30age_male_value,
    'negative_30age_female' : negative_30age_female_value,
    'postive_40age_male' : postive_40age_male_value,
    'postive_40age_female' : postive_40age_female_value,
    'negative_40age_male' : negative_40age_male_value,
    'negative_40age_female' : negative_40age_female_value,
    'postive_50age_male' : postive_50age_male_value,
    'postive_50age_female' : postive_50age_female_value,
    'negative_50age_male' : negative_50age_male_value,
    'negative_50age_female' : negative_50age_female_value,
    'postive_60age_male' : postive_60age_male_value,
    'postive_60age_female' : postive_60age_female_value,
    'negative_60age_male' : negative_60age_male_value,
    'negative_60age_female' : negative_60age_female_value,
  }

  return result

# 데일리 데이터 정리해서 보내는 부분
def today_dailydata(objects):
  start_day = datetime.date.today() - datetime.timedelta(days=7)
  end_day = datetime.date.today()
  dailydatas = objects.dailydata_set.filter(created_at__gte=start_day, created_at__lte=end_day)

  daily_data = {}
  for data in dailydatas:
    total = data.postive_count + data.negative_count
    postive_per = (data.postive_count/total*100) if not (total == 0) else 0
    negative_per = (data.negative_count/total*100) if not (total == 0) else 0
    daily_data[data.created_at.date().strftime("%Y-%m-%d")] = {
      'postive' : postive_per,
      'negative' : negative_per,
    }
  return daily_data


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
  topics = Topic.objects.all().order_by('-created_at')
  hot = Topic.objects.filter(hot_topic=True)

  return render(request, 'topic/list.html', {
    'topics': topics,
    'hot':hot,
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

@login_required(login_url='/auth/signin/')
@user_passes_test(lambda u: u.gender and u.age_range, login_url='/auth/add_info/')
def topic_result(request, topic_id):
  topic = Topic.objects.get(pk=topic_id)
  selections = topic.selection_set.all()

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
    'data': data,
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
      # age, gender 부분 유저 정보로 바꿔줘야함.
      selection, is_selection = Selection.objects.get_or_create(topic=topic, selector=user, age_range=10, gender=1)
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