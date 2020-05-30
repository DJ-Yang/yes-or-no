from yorn.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

SOCIALACCOUNT_PROVIDERS = {
    'kakao': {
        'APP': {
            'client_id' : '9c0f252154e03204b20da14dd74d775f',
            'redirect_uri' : 'http://homevalue.co.kr/auth/accounts/kakao/login/callback/',
            'response_type' : 'code',        
        }
    }
}

CRONTAB_COMMAND_SUFFIX = '2>&1'
CRONTAB_DJANGO_SETTINGS_MODULE = 'yorn.settings.prod'
CRONJOBS = [
    ('0 0 * * *', 'topic.views.set_hot_topic', '>>'+ os.path.join(BASE_DIR, 'data.log'),)
]