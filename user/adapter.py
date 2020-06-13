from django.conf import settings
from django.shortcuts import resolve_url, redirect, HttpResponseRedirect
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from user.models import User
from allauth.socialaccount.models import SocialAccount
import json

class MyAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):      

        # signin view와 마찬가지 방법
        # request.GET에서 못가져오는 이유는 signin view에서 바로여기로 오는게 아니기 때문
        # signin -> kakao/login/callback/?겁나긴 토큰params 에서 이 함수가 호출됨
        # 때문에 중간에서 로그인페이지에서 지정한 next_page 파라미터는 사라져있음

        _next = request.META.get('HTTP_REFERER')
        _next = _next.split('next_page=',maxsplit=3)[1]
        url = _next
        user = User.objects.get(pk=request.user.id)

        if user.gender and user.age_range:
            return url
        else:
            return '/auth/add_info/'

    def get_logout_redirect_url(self, request):
        return resolve_url(settings.LOGOUT_REDIRECT_URL)


class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        # social account user
        user = super(MySocialAccountAdapter, self).save_user(request, sociallogin, form)
    
        social_app_name = sociallogin.account.provider.upper()
        extra_data = SocialAccount.objects.get(user=user).extra_data
        if social_app_name == "KAKAO":
            User.objects.get_or_create_kakao_user(user_pk=user.pk, extra_data=extra_data)
            return user
        else:
            return user

    def populate_user(self, request, sociallogin, data):
        # 내가 커스탐한 user
        user = super(MySocialAccountAdapter, self).populate_user(request,sociallogin, data)
        
        return user
        