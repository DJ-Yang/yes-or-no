from django.shortcuts import render


def signin(request):
    return render(request, 'user/signin.html')
