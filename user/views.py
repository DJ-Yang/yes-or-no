from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from .forms import AddForm
from .models import User


def signin(request):
    if request.GET.get('next_page',''):
        return render(request, 'user/signin.html')
    else:
        _next = request.META.get('HTTP_REFERER')
        _next = _next.split('/',maxsplit=3)[3]

        url = '/auth/signin/?next_page=/%s' % _next
        return HttpResponseRedirect(url)


def add_info(request):

    wrong_flag = User.objects.get(pk=request.user.id)
    # 계속 수정해야할때 들어가야되서 일부러 not 넣어둠 나중에 지워야함.
    if wrong_flag.gender and not (wrong_flag.age_range == 0):
        return redirect('topic:list')
    else:
        if request.method == 'POST':
            form = AddForm(request.POST)
            if form.is_valid():
                user = User.objects.get(pk=request.user.id)
                user.age_range = form.cleaned_data['age_range']
                user.gender = form.cleaned_data['gender']
                user.save()
                return redirect('topic:list')
        else:
            form = AddForm
            context = {'form':form}
        return render(request, 'user/add_info.html', context)