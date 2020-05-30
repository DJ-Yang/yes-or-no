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

# 임시 스태틱 루트 설정
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# AWS_LOCATION = 'static'
# AWS_REGION = get_secret("AWS_REGION")
# AWS_STORAGE_BUCKET_NAME = get_secret("AWS_STORAGE_BUCKET_NAME")
# AWS_ACCESS_KEY_ID = get_secret("AWS_ACCESS_KEY_ID")
# AWS_SECRET_ACCESS_KEY = get_secret("AWS_SECRET_ACCESS_KEY")
# AWS_QUERYSTRING_AUTH = False
# AWS_S3_HOST = 's3.%s.amazonaws.com' % AWS_REGION
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# # Static Setting
# STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
# STATICFILES_LOCATION = 'static'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# # Media Setting
# MEDIA_URL = "https://%s/media/" % AWS_S3_CUSTOM_DOMAIN
# MEDIAFILES_LOCATION = 'media'
# DEFAULT_FILE_STORAGE = 'yorn.settings.storage_backends.MediaStorage'

# # # Root Setting
# # STATIC_ROOT = '%s/static' % STORAGE_PATH
# # MEDIA_ROOT = '%s/media' % STORAGE_PATH