from django.conf import settings
from django.shortcuts import resolve_url
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from user.models import User
from allauth.socialaccount.models import SocialAccount


class MyAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):      
        print('login')  
        return settings.LOGIN_REDIRECT_URL        

    def get_logout_redirect_url(self, request):
        print('logout')
        return resolve_url(settings.LOGOUT_REDIRECT_URL)


class MySocialAccountAdapter(DefaultSocialAccountAdapter):

    def save_user(self, request, sociallogin, form=None):
        user = super(MySocialAccountAdapter, self).save_user(request, sociallogin, form)

        social_app_name = sociallogin.account.provider.upper()
        extra_data = SocialAccount.objects.get(user=user).extra_data

        if social_app_name == "KAKAO":
            User.objects.get_or_create_kakao_user(user_pk=user.pk, extra_data=extra_data)


