import os
from .settings import *  # noqa


VIRTUAL_HOST = os.getenv('VIRTUAL_HOST')
ALLOWED_HOSTS = [
    # For deploy
    VIRTUAL_HOST,
]

CSRF_TRUSTED_ORIGINS = [
    'https://' + VIRTUAL_HOST,
]

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = False
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'ithuan',
        'HOST': 'postgres',
        'PORT': '',
    }
}

STATIC_ROOT = '/staticfiles/'
