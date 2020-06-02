from django.conf import settings
from django.shortcuts import resolve_url, redirect
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from user.models import User
from allauth.socialaccount.models import SocialAccount
import json

class MyAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):      
        print('login')  
        
        user = User.objects.get(pk=request.user.id)

        if user.gender and user.age_range:
            return settings.LOGIN_REDIRECT_URL        
        else:
            return '/auth/add_info/'

    def get_logout_redirect_url(self, request):
        print('logout')
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