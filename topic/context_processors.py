from django.conf import settings

def kakao_secret_key(request):
  return {'KAKAO_KEY': settings.KAKAO_APP_KEY}
