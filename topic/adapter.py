from django.conf import settings
from django.shortcuts import resolve_url, render, redirect
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.adapter import get_adapter as get_account_adapter


# django allauth 에서 redirect url 커스텀 하려면 settings 에서 REDIRECT_URL 설정으로는 적용이 안됨
class MyAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        return settings.LOGIN_REDIRECT_URL        

    def get_logout_redirect_url(self, request):
        return resolve_url(settings.LOGOUT_REDIRECT_URL)