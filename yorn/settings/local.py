from yorn.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

SOCIALACCOUNT_PROVIDERS = {    
    'kakao': {
        'APP': {
            'client_id' : '9c0f252154e03204b20da14dd74d775f',
            'response_type' : 'code',        
        }
    }
}