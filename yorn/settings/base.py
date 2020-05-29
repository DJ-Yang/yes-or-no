import os
import json

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
secret_file = os.path.join(BASE_DIR, 'secrets.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} enviroment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_secret("SECRET_KEY")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'topic.apps.TopicConfig',
    'user.apps.UserConfig',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.kakao',
    'django_crontab',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'yorn.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'yorn.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# allauth setting

AUTH_USER_MODEL = 'user.User'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1

ACCOUNT_ADAPTER = 'user.adapter.MyAccountAdapter'
SOCIALACCOUNT_ADAPTER = 'user.adapter.MySocialAccountAdapter'

LOGIN_REDIRECT_URL = '/topic/'
LOGOUT_REDIRECT_URL = '/topic/'

ACCOUNT_LOGOUT_ON_GET = True
SOCIALACCOUNT_PROVIDERS = {
    'kakao': {
        'APP': {
            'client_id' : '9c0f252154e03204b20da14dd74d775f',
            'redirect_uri' : 'http://127.0.0.1:8000/auth/accounts/kakao/login/callback/',
            'response_type' : 'code',        
        }
    }
}

CRONTAB_COMMAND_SUFFIX = '2>&1'
CRONTAB_DJANGO_SETTINGS_MODULE = 'yorn.settings.local'
CRONJOBS = [
    ('0 0 * * *', 'topic.views.set_hot_topic', '>>'+ os.path.join(BASE_DIR, 'data.log'),)
]

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