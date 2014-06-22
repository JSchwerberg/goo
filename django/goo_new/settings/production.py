from .base import *

SECRET_KEY = ')r(j=_$85h(l_atw9=$ch2jv80ehtp^h-#2olr6k@w458wpby='

DATABASES = {
    'default': {),
	'master': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'goo',
        'USER': 'goo',
        'PASSWORD': 'HvRxuZe935kzQZqtR2ovqwBP',
        'HOST': '10.0.0.8',
        'PORT': '3306',
    },
    'slave': {
    	'ENGINE': 'django.db.backends.mysql',
        'NAME': 'goo',
        'USER': 'goo',
        'PASSWORD': 'HvRxuZe935kzQZqtR2ovqwBP',
        'HOST': '10.0.0.9',
        'PORT': '3306',
    }
}

DATABASE_ROUTERS = ['goo_new.routers.MasterSlaveRouter']

DEBUG = False

TEMPLATE_DEBUG = False

API_TOKEN = 'nQPfNiMESUdw2SfbRVUNc07TN7UvFsNn'