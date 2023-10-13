import os
from pathlib import Path
from decouple import config
import logging

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-l5+=&fbwi_zfr9ag=&^-&vmg&6_!1=^i3ym8a08oxs)vx!lpq5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    'newapp',

    'django.contrib.sites',
    'django.contrib.flatpages',

    'django_filters',

    'django_apscheduler',
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

ROOT_URLCONF = 'news_paper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
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

WSGI_APPLICATION = 'news_paper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

SITE_ID=1

LOGIN_URL = '/login/'

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]



SITE_ID = 1

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

LOGIN_URL = 'http://127.0.0.1:8000/accounts/login/'
LOGIN_REDIRECT_URL = 'http://127.0.0.1:8000/news/'

ACCOUNT_FORMS = {'signup': 'newapp.models.CommonSignupForm'}

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "Eugen"
EMAIL_HOST_PASSWORD = 'Qwerty12223'
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = 'e.cool7@yandex.ru'

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'), # Указываем, куда будем сохранять кэшируемые файлы! Не забываем создать папку cache_files внутри папки с manage.py!
    }
}
ADMINS = [("Eugen", "e.cool7@yandex.ru")]

LOGGING_DIR = os.path.join(BASE_DIR, 'logs')
os.makedirs(LOGGING_DIR, exist_ok=True)

LOGGING = {
     'version': 1,
     'disable_existing_loggers': False,
     'filters': {
         'require_debug_true': {
             '()': 'django.utils.log.RequireDebugTrue',
         },
         'require_debug_false': {
             '()': 'django.utils.log.RequireDebugFalse',
         },
     },
     'formatters': {
         'formatter_debug': {
             'format': '{asctime} - {levelname} - {message}\n',
             'style': '{',
         },
         'formatter_warning': {
             'format': '{asctime} - {levelname} - {message} - {pathname}\n',
             'style': '{',
         },
         'formatter_error': {
             'format': '{asctime} - {levelname} - {message} - {pathname} - {exc_info}\n',
             'style': '{',
         },
         'formatter_info': {
             'format': '{asctime} - {levelname} - {module} - {message}\n',
             'style': '{',
         },
     },
     'handlers': {
         'console_debug': {
             'level': 'DEBUG',
             'class': 'logging.StreamHandler',
             'formatter': 'formatter_debug',
             'filters': ['require_debug_true'],
         },
         'console_warning': {
             'level': 'WARNING',
             'class': 'logging.StreamHandler',
             'formatter': 'formatter_warning',
             'filters': ['require_debug_true'],
         },
         'console_error': {
             'level': 'ERROR',
             'class': 'logging.StreamHandler',
             'formatter': 'formatter_error',
             'filters': ['require_debug_true'],
         },
         'file_info': {
             'level': 'INFO',
             'class': 'logging.FileHandler',
             'filename': 'general.log',
             'formatter': 'formatter_info',
             'filters': ['require_debug_false'],
         },
         'file_error': {
             'level': 'ERROR',
             'class': 'logging.FileHandler',
             'filename': 'errors.log',
             'formatter': 'formatter_error',
         },
         'file_security': {
             'level': 'DEBUG',
             'class': 'logging.FileHandler',
             'filename': 'security.log',
             'formatter': 'formatter_info',
         },
         'mail_error': {
             'level': 'ERROR',
             'class': 'django.utils.log.AdminEmailHandler',
             'formatter': 'formatter_warning',
             'filters': ['require_debug_false'],
         },
         'mail_handler': {
             'level': 'ERROR',
             'class': 'logging.handlers.SMTPHandler',
             'mailhost': (EMAIL_HOST, EMAIL_PORT),
             'fromaddr': EMAIL_HOST_USER,
             'toaddrs': [admin[1] for admin in ADMINS],
             'subject': '[Django Error] Critical error on your Django site',
             'credentials': (EMAIL_HOST_USER, EMAIL_HOST_PASSWORD),
             'secure': (),
         },
     },
     'loggers': {
         'django': {
             'handlers': ['console_debug', 'console_warning', 'console_error', 'file_info'],
             'level': 'DEBUG',
             'propagate': True,
         },
         'django.request': {
             'handlers': ['file_error', 'mail_error', 'mail_handler'],
             'level': 'ERROR',
             'propagate': True,
         },
         'django.server': {
             'handlers': ['file_error', 'mail_error', 'mail_handler'],
             'level': 'ERROR',
             'propagate': True,
         },
         'django.template': {
             'handlers': ['file_error'],
             'level': 'ERROR',
             'propagate': True,
         },
         'django.db_backends': {
             'handlers': ['file_error'],
             'level': 'ERROR',
             'propagate': True,
         },
         'django.security': {
             'handlers': ['file_security'],
             'level': 'DEBUG',
             'propagate': True,
         },
     },
 }