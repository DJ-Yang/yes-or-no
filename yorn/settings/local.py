from yorn.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

SOCIALACCOUNT_PROVIDERS = {
    'kakao': {
        'APP': {
            'client_id' : '9c0f252154e03204b20da14dd74d775f',
            'redirect_url' : 'http://127.0.0.1:8000/auth/accounts/kakao/login/callback/',
            'response_type' : 'code',        
        }
    }
}

CRONTAB_COMMAND_SUFFIX = '2>&1'
CRONTAB_DJANGO_SETTINGS_MODULE = 'yorn.settings.local'
CRONJOBS = [
    ('* * * * *', 'topic.views.set_hot_topic', '>>'+ os.path.join(BASE_DIR, 'data.log'),)
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
