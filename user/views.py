from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import AddForm, regionForm
from .models import User


def signin(request):
        return render(request, 'user/signin.html')
    


def add_info(request):
    wrong_flag = User.objects.get(pk=request.user.id)
    # 계속 수정해야할때 들어가야되서 일부러 not 넣어둠 나중에 지워야함.
    if wrong_flag.gender and not (wrong_flag.age_range == 0):
        return redirect('topic:list')
    else:
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