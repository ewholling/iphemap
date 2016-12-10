"""
Settings for iphemap.
Now hosted on VPS at 
"""

import os
import imp

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DEBUG = True

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

ALLOWED_HOSTS = ['*']

SECRET_KEY = 'vm4rl5*ymb@2&d_(gc$gb-^twq9w(u69hi--%$5xrh!xk(t%hw'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ipscdb',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
          'context_processors' : [
            'django.contrib.auth.context_processors.auth',
          ]},
    },
]

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'data', 'db.sqlite3'),
  }
}


STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static')
STATIC_URL = '/static/'

LOCKDOWN_PASSWORDS = ('imitola', )
LOCKDOWN_FORM = 'lockdown.forms.LockdownForm'
