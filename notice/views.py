from django.shortcuts import render
from .models import Notice

# Create your views here.
def notice(request):
  notice = Notice.objects.all().order_by('-created_at')

  context = {'notice':notice}
  return render(request, 'notice/notice.html', context)

def notice_detail(request, id):
  notice = Notice.objects.get(pk=id)
  context = {'notice':notice}
  return render(request, 'notice/notice_detail.html', context)