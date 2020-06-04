from yorn.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'homevalue.co.kr', 'www.homevale.co.kr']

SOCIALACCOUNT_PROVIDERS = {
    'kakao': {
        'APP': {
            'client_id' : '9c0f252154e03204b20da14dd74d775f',
            'response_type' : 'code',        
        }
    }
}