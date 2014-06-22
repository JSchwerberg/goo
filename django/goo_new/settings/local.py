from .base import *

SECRET_KEY = '=c30)ysmf7$rsbsj^dm%(sv)4pbazp2^u-&_f9)phq&!b)$24-'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'goo_new',
        'USER': 'goo',
        'PASSWORD': 'adGTySyG6unc6E8ptHr3y9pD',
    }
}


DEBUG = True

TEMPLATE_DEBUG = True

API_TOKEN = 'aqb7YPH5zRkpza3oLG2irwFRd6fArHVq'