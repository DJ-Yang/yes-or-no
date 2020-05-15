from django.shortcuts import render
from .models import Topic, Selection
from django.http import HttpResponse, JsonResponse

# Create your views here.

def topic_list(request):
  topics = Topic.objects.all()

  return render(request, 'topic/list.html', {
    'topics': topics,
  })

def select(request, topic_id):
  topic = Topic.objects.get(pk=topic_id)

  return render(request, 'topic/select.html', {
    'topic': topic,
  })

def set_selection(request):
  if request.method == 'POST':
    select_type = int(request.POST.get('type'))
    topic_id = int(request.POST.get('topic_id'))
    topic = Topic.objects.get(pk=topic_id)
    user = request.user
    # age, sex 부분 유저 정보로 바꿔줘야함.
    selection, is_selection = Selection.objects.get_or_create(topic=topic, selector=user, age=1, sex=1)
    if is_selection:
      selection.select = select_type
      selection.save()
    else:
      selection.select = select_type
      selection.save()
    b = {
      'status': '성공'
    }
    return JsonResponse(b)