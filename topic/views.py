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

# def create_daily_data():
#   topics = Topic.objects.all()
  
#   for topic in topics:
#     selections = topic.selection_set.all()
#     total = selections.count()
#     positive = selections.filter(select=0)
#     negative = selections.filter(select=1)
#     positive_male = positive.filter(gender=0)
#     positive_female = positive.filter(gender=1)
#     negative_male = negative.filter(gender=0)
#     negative_female = negative.filter(gender=1)
#     positive_10age = positive.filter(age_range=10)
#     positive_10age_male = positive_10age.filter(gender=0)
#     positive_10age_female = positive_10age.filter(gender=1)
#     positive_20age = positive.filter(age_range=20)
#     positive_20age_male = positive_20age.filter(gender=0)
#     positive_20age_female = positive_20age.filter(gender=1)
#     positive_30age = positive.filter(age_range=30)
#     positive_30age_male = positive_30age.filter(gender=0)
#     positive_30age_female = positive_30age.filter(gender=1)
#     positive_40age = positive.filter(age_range=40)
#     positive_40age_male = positive_40age.filter(gender=0)
#     positive_40age_female = positive_40age.filter(gender=1)
#     positive_50age = positive.filter(age_range=50)
#     positive_50age_male = positive_50age.filter(gender=0)
#     positive_50age_female = positive_50age.filter(gender=1)
#     positive_60age = positive.filter(age_range=60)
#     positive_60age_male = positive_60age.filter(gender=0)
#     positive_60age_female = positive_60age.filter(gender=1)
#     negative_10age = negative.filter(age_range=10)
#     negative_10age_male = negative_10age.filter(gender=0)
#     negative_10age_female = negative_10age.filter(gender=1)
#     negative_20age = negative.filter(age_range=20)
#     negative_20age_male = negative_20age.filter(gender=0)
#     negative_20age_female = negative_20age.filter(gender=1)
#     negative_30age = negative.filter(age_range=30)
#     negative_30age_male = negative_30age.filter(gender=0)
#     negative_30age_female = negative_30age.filter(gender=1)
#     negative_40age = negative.filter(age_range=40)
#     negative_40age_male = negative_40age.filter(gender=0)
#     negative_40age_female = negative_40age.filter(gender=1)
#     negative_50age = negative.filter(age_range=50)
#     negative_50age_male = negative_50age.filter(gender=0)
#     negative_50age_female = negative_50age.filter(gender=1)
#     negative_60age = negative.filter(age_range=60)
#     negative_60age_male = negative_60age.filter(gender=0)
#     negative_60age_female = negative_60age.filter(gender=1)


#     data = DailyData()
#     data.topic = topic
#     data.positive_count = positive.count()
#     data.negative_count = negative.count()
#     data.positive_male_count = positive_male.count()
#     data.positive_female_count = positive_female.count()
#     data.negative_male_count = negative_male.count()
#     data.negative_female_count = negative_female.count()
#     data.positive_10age_count = positive_10age.count()
#     data.positive_10age_male_count = positive_10age_male.count()
#     data.positive_10age_female_count = positive_10age_female.count()
#     data.positive_20age_count = positive_20age.count()
#     data.positive_20age_male_count = positive_20age_male.count()
#     data.positive_20age_female_count = positive_20age_female.count()
#     data.positive_30age_count = positive_30age.count()
#     data.positive_30age_male_count = positive_30age_male.count()
#     data.positive_30age_female_count = positive_30age_female.count()
#     data.positive_40age_count = positive_40age.count()
#     data.positive_40age_male_count = positive_40age_male.count()
#     data.positive_40age_female_count = positive_40age_female.count()
#     data.positive_50age_count = positive_50age.count()
#     data.positive_50age_male_count = positive_50age_male.count()
#     data.positive_50age_female_count = positive_50age_female.count()
#     data.positive_60age_count = positive_60age.count()
#     data.positive_60age_male_count = positive_60age_male.count()
#     data.positive_60age_female_count = positive_60age_female.count()
#     data.negative_10age_count = negative_10age.count()
#     data.negative_10age_male_count = negative_10age_male.count()
#     data.negative_10age_female_count = negative_10age_female.count()
#     data.negative_20age_count = negative_20age.count()
#     data.negative_20age_male_count = negative_20age_male.count()
#     data.negative_20age_female_count = negative_20age_female.count()
#     data.negative_30age_count = negative_30age.count()
#     data.negative_30age_male_count = negative_30age_male.count()
#     data.negative_30age_female_count = negative_30age_female.count()
#     data.negative_40age_count = negative_40age.count()
#     data.negative_40age_male_count = negative_40age_male.count()
#     data.negative_40age_female_count = negative_40age_female.count()
#     data.negative_50age_count = negative_50age.count()
#     data.negative_50age_male_count = negative_50age_male.count()
#     data.negative_50age_female_count = negative_50age_female.count()
#     data.negative_60age_count = negative_60age.count()
#     data.negative_60age_male_count = negative_60age_male.count()
#     data.negative_60age_female_count = negative_60age_female.count()

#     data.save()

# def today_caculate_per(objects, topic):
#   total = objects.count()
#   positive = objects.filter(select=0)
#   negative = objects.filter(select=1)
#   male = objects.filter(gender=0)
#   female = objects.filter(gender=1)
#   age10 = objects.filter(age_range=10)
#   age20 = objects.filter(age_range=20)
#   age30 = objects.filter(age_range=30)
#   age40 = objects.filter(age_range=40)
#   age50 = objects.filter(age_range=50)
#   age60 = objects.filter(age_range=60)
#   positive_male = positive.filter(gender=0)
#   positive_female = positive.filter(gender=1)
#   negative_male = negative.filter(gender=0)
#   negative_female = negative.filter(gender=1)
#   positive_10age = positive.filter(age_range=10)
#   positive_10age_male = positive_10age.filter(gender=0)
#   positive_10age_female = positive_10age.filter(gender=1)
#   positive_20age = positive.filter(age_range=20)
#   positive_20age_male = positive_20age.filter(gender=0)
#   positive_20age_female = positive_20age.filter(gender=1)
#   positive_30age = positive.filter(age_range=30)
#   positive_30age_male = positive_30age.filter(gender=0)
#   positive_30age_female = positive_30age.filter(gender=1)
#   positive_40age = positive.filter(age_range=40)
#   positive_40age_male = positive_40age.filter(gender=0)
#   positive_40age_female = positive_40age.filter(gender=1)
#   positive_50age = positive.filter(age_range=50)
#   positive_50age_male = positive_50age.filter(gender=0)
#   positive_50age_female = positive_50age.filter(gender=1)
#   positive_60age = positive.filter(age_range=60)
#   positive_60age_male = positive_60age.filter(gender=0)
#   positive_60age_female = positive_60age.filter(gender=1)
#   negative_10age = negative.filter(age_range=10)
#   negative_10age_male = negative_10age.filter(gender=0)
#   negative_10age_female = negative_10age.filter(gender=1)
#   negative_20age = negative.filter(age_range=20)
#   negative_20age_male = negative_20age.filter(gender=0)
#   negative_20age_female = negative_20age.filter(gender=1)
#   negative_30age = negative.filter(age_range=30)
#   negative_30age_male = negative_30age.filter(gender=0)
#   negative_30age_female = negative_30age.filter(gender=1)
#   negative_40age = negative.filter(age_range=40)
#   negative_40age_male = negative_40age.filter(gender=0)
#   negative_40age_female = negative_40age.filter(gender=1)
#   negative_50age = negative.filter(age_range=50)
#   negative_50age_male = negative_50age.filter(gender=0)
#   negative_50age_female = negative_50age.filter(gender=1)
#   negative_60age = negative.filter(age_range=60)
#   negative_60age_male = negative_60age.filter(gender=0)
#   negative_60age_female = negative_60age.filter(gender=1)

#   # 일일 투표 데이터 비율
#   positive_value = (positive.count()/total*100) if not(total == 0) else 0
#   negative_value = (negative.count()/total*100) if not(total == 0) else 0

#   # 전체 데이터
#   positive_10age_male_value = (positive_10age_male.count()/total*100) if not(total == 0) else 0
#   positive_10age_female_value = (positive_10age_female.count()/total*100) if not(total == 0) else 0
#   negative_10age_male_value = (negative_10age_male.count()/total*100) if not(total == 0) else 0
#   negative_10age_female_value = (negative_10age_female.count()/total*100) if not(total == 0) else 0
#   positive_20age_male_value = (positive_20age_male.count()/total*100) if not(total == 0) else 0
#   positive_20age_female_value = (positive_20age_female.count()/total*100) if not(total == 0) else 0
#   negative_20age_male_value = (negative_20age_male.count()/total*100) if not(total == 0) else 0
#   negative_20age_female_value = (negative_20age_female.count()/total*100) if not(total == 0) else 0
#   positive_30age_male_value = (positive_30age_male.count()/total*100) if not(total == 0) else 0
#   positive_30age_female_value = (positive_30age_female.count()/total*100) if not(total == 0) else 0
#   negative_30age_male_value = (negative_30age_male.count()/total*100) if not(total == 0) else 0
#   negative_30age_female_value = (negative_30age_female.count()/total*100) if not(total == 0) else 0
#   positive_40age_male_value = (positive_40age_male.count()/total*100) if not(total == 0) else 0
#   positive_40age_female_value = (positive_40age_female.count()/total*100) if not(total == 0) else 0
#   negative_40age_male_value = (negative_40age_male.count()/total*100) if not(total == 0) else 0
#   negative_40age_female_value = (negative_40age_female.count()/total*100) if not(total == 0) else 0
#   positive_50age_male_value = (positive_50age_male.count()/total*100) if not(total == 0) else 0
#   positive_50age_female_value = (positive_50age_female.count()/total*100) if not(total == 0) else 0
#   negative_50age_male_value = (negative_50age_male.count()/total*100) if not(total == 0) else 0
#   negative_50age_female_value = (negative_50age_female.count()/total*100) if not(total == 0) else 0
#   positive_60age_male_value = (positive_60age_male.count()/total*100) if not(total == 0) else 0
#   positive_60age_female_value = (positive_60age_female.count()/total*100) if not(total == 0) else 0
#   negative_60age_male_value = (negative_60age_male.count()/total*100) if not(total == 0) else 0
#   negative_60age_female_value = (negative_60age_female.count()/total*100) if not(total == 0) else 0
  
#   # 성별 데이터
#   positive_male_value = (positive_male.count()/male.count()*100) if not (male.count() == 0) else 0
#   positive_female_value = (positive_female.count()/female.count()*100) if not (female.count() == 0) else 0
#   negative_male_value = (negative_male.count()/male.count()*100) if not (male.count() == 0) else 0
#   negative_female_value = (negative_female.count()/female.count()*100) if not (female.count() == 0) else 0

#   # 연령별 데이터
#   positive_10age_value = (positive_10age.count()/age10.count()*100) if not (age10.count() == 0) else 0
#   positive_20age_value = (positive_20age.count()/age20.count()*100) if not (age20.count() == 0) else 0
#   positive_30age_value = (positive_30age.count()/age30.count()*100) if not (age30.count() == 0) else 0
#   positive_40age_value = (positive_40age.count()/age40.count()*100) if not (age40.count() == 0) else 0
#   positive_50age_value = (positive_50age.count()/age50.count()*100) if not (age50.count() == 0) else 0
#   positive_60age_value = (positive_60age.count()/age60.count()*100) if not (age60.count() == 0) else 0
#   negative_10age_value = (negative_10age.count()/age10.count()*100) if not (age10.count() == 0) else 0
#   negative_20age_value = (negative_20age.count()/age20.count()*100) if not (age20.count() == 0) else 0
#   negative_30age_value = (negative_30age.count()/age30.count()*100) if not (age30.count() == 0) else 0
#   negative_40age_value = (negative_40age.count()/age40.count()*100) if not (age40.count() == 0) else 0
#   negative_50age_value = (negative_50age.count()/age50.count()*100) if not (age50.count() == 0) else 0
#   negative_60age_value = (negative_60age.count()/age60.count()*100) if not (age60.count() == 0) else 0
  
#   # 주별, 월별, 연별(보류) 데이터 다른 함수로 만들기

#   result = {
#     'positive' : int(positive_value),
#     'negative' : int(negative_value),
#     'positive_male' : int(positive_male_value),
#     'positive_female' : int(positive_female_value),
#     'negative_male' : int(negative_male_value),
#     'negative_female' : int(negative_female_value),
#     'positive_10age' : int(positive_10age_value),
#     'positive_20age' : int(positive_20age_value),
#     'positive_30age' : int(positive_30age_value),
#     'positive_40age' : int(positive_40age_value),
#     'positive_50age' : int(positive_50age_value),
#     'positive_60age' : int(positive_60age_value),
#     'negative_10age' : int(negative_10age_value),
#     'negative_20age' : int(negative_20age_value),
#     'negative_30age' : int(negative_30age_value),
#     'negative_40age' : int(negative_40age_value),
#     'negative_50age' : int(negative_50age_value),
#     'negative_60age' : int(negative_60age_value),
#     'positive_10age_male' : int(positive_10age_male_value),
#     'positive_10age_female' : int(positive_10age_female_value),
#     'negative_10age_male' : int(negative_10age_male_value),
#     'negative_10age_female' : int(negative_10age_female_value),
#     'positive_20age_male' : int(positive_20age_male_value),
#     'positive_20age_female' : int(positive_20age_female_value),
#     'negative_20age_male' : int(negative_20age_male_value),
#     'negative_20age_female' : int(negative_20age_female_value),
#     'positive_30age_male' : int(positive_30age_male_value),
#     'positive_30age_female' : int(positive_30age_female_value),
#     'negative_30age_male' : int(negative_30age_male_value),
#     'negative_30age_female' : int(negative_30age_female_value),
#     'positive_40age_male' : int(positive_40age_male_value),
#     'positive_40age_female' : int(positive_40age_female_value),
#     'negative_40age_male' : int(negative_40age_male_value),
#     'negative_40age_female' : int(negative_40age_female_value),
#     'positive_50age_male' : int(positive_50age_male_value),
#     'positive_50age_female' : int(positive_50age_female_value),
#     'negative_50age_male' : int(negative_50age_male_value),
#     'negative_50age_female' : int(negative_50age_female_value),
#     'positive_60age_male' : int(positive_60age_male_value),
#     'positive_60age_female' : int(positive_60age_female_value),
#     'negative_60age_male' : int(negative_60age_male_value),
#     'negative_60age_female' : int(negative_60age_female_value),
#   }

#   return result

# 데일리 데이터 정리해서 보내는 부분
# def today_dailydata(objects):
#   start_day = datetime.date.today() - datetime.timedelta(days=7)
#   end_day = datetime.date.today()
#   dailydatas = objects.dailydata_set.filter(created_at__gte=start_day, created_at__lte=end_day)

#   daily_data = {}
#   for data in dailydatas:
#     total = data.positive_count + data.negative_count
#     positive_per = (data.positive_count/total*100) if not (total == 0) else 0
#     negative_per = (data.negative_count/total*100) if not (total == 0) else 0
#     daily_data[data.created_at.date().strftime("%Y-%m-%d")] = {
#       'positive' : positive_per,
#       'negative' : negative_per,
#     }
#   return daily_data


# 핫 토픽 설정 부분
# updated_at 필드를 추가해서 기존에 설문에 참여했던 사람이 값을 변경했을 경우도 값에 포함될 수 있게 함.
# 매일 오전 00시 00분에 실행되게 데코레이터 사용
# def set_hot_topic():
#   yesterday = datetime.date.today() - datetime.timedelta(days=1)
#   today_selections = Selection.objects.filter(updated_at__date=yesterday)

#   topic_list = {
#   }
#   hot_topic_list = []

#   for selection in today_selections:
#     if selection.topic.id in topic_list:
#       topic_list[selection.topic.id] += 1
#     else:
#       topic_list[selection.topic.id] = 1

#   topic_list = sorted(topic_list.items(), key=(lambda x : x[0]), reverse=True)

#   for topic in topic_list:
#     if len(hot_topic_list) >= 3:
#       if hot_topic_list[2][1] < topic[1]:
#         hot_topic_list[2] = topic
#     else:
#       hot_topic_list.append(topic)
#     hot_topic_list = sorted(hot_topic_list, key=(lambda x : x[1]), reverse=True)

#   hot_topic_id = convert(hot_topic_list)

#   test = Topic.objects.filter(hot_topic=True).update(hot_topic=False)

#   Topic.objects.filter(id__in=hot_topic_id).update(hot_topic=True)

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