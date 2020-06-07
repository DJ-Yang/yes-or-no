from yorn.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'topic-talk.com', 'www.topic-talk.com']

SOCIALACCOUNT_PROVIDERS = {
    'kakao': {
        'APP': {
            'client_id' : '9c0f252154e03204b20da14dd74d775f',
            'response_type' : 'code',        
        }
    }
}