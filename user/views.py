from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import AddForm, regionForm, EditForm
from .models import User
from topic.models import Pick
from point.models import Point

def signin(request):
        return render(request, 'user/signin.html')
def add_info(request):
    # wrong_flag = User.objects.get(pk=request.user.id)
    # 계속 수정해야할때 들어가야되서 일부러 not 넣어둠 나중에 지워야함.
    if request.method == 'POST':
        addform = AddForm(request.POST)
        regionform = regionForm(request.POST)
        if addform.is_valid() and regionform.is_valid():
            user = User.objects.get(pk=request.user.id)
            user.age_range = addform.cleaned_data['age_range']
            user.gender = addform.cleaned_data['gender']
            user.sido = regionform.cleaned_data['sido']
            user.sigungu = regionform.cleaned_data['sigungu']
            user.save()
        return redirect('topic:list')
    else:
        addform = AddForm()
        regionform = regionForm()
        context = {'addform':addform,'regionform':regionform}
        return render(request, 'user/add_info.html', context)

def get_form(request):
    form = regionForm()
    form = form.set_region(selected_sido=request.GET.get('sido','서울'))
    return HttpResponse(form)


def user_info(request):

    user = User.objects.get(pk=request.user.pk)
    
    # 포인트 올리기
    # p = Point.objects.addPoint(request.user.point.pk,100)

    context = {
        'user':user,
        'picks':Pick.objects.filter(author=request.user).order_by('-updated_at')
    }
    return render(request, 'user/user_info.html', context)

def edit_profile(request):
    if request.method == 'POST':
        editform = EditForm(request.POST)
        regionform = regionForm(request.POST)
        if editform.is_valid() and regionform.is_valid():
            user = User.objects.get(pk=request.user.id)
            # user.nickname = editform.cleaned_data['nickname']
            user.age_range = editform.cleaned_data['age_range']
            user.gender = editform.cleaned_data['gender']
            user.sido = regionform.cleaned_data['sido']
            user.sigungu = regionform.cleaned_data['sigungu']
            user.save()
        return redirect('user_info')
    else:            
        editform = EditForm()
        regionform = regionForm().set_region(selected_sido=request.user.sido)
        
        user_data = ''+request.user.nickname+','+str(request.user.age_range)+','+request.user.gender
        context = {
            'editform':editform,
            'regionform':regionform,
            'user_data':user_data
        }

        return render(request, 'user/edit_profile.html', context)