from .base import *
import ldap
from django_auth_ldap.config import LDAPSearch, LDAPSearchUnion

SECRET_KEY = ')r(j=_$85h(l_atw9=$ch2jv80ehtp^h-#2olr6k@w458wpby='

DEBUG = False

TEMPLATE_DEBUG = False

DEFAULT_DB_ALIAS = 'master'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'goo',
        'USER': 'goo',
        'PASSWORD': 'HvRxuZe935kzQZqtR2ovqwBP',
        'HOST': '10.0.0.8',
        'PORT': '3306',
    },
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

PAYPAL_RECEIVER_EMAIL = "basnipa@gmail.com"

API_TOKEN = 'nQPfNiMESUdw2SfbRVUNc07TN7UvFsNn'

AUTHENTICATION_BACKENDS= (
	'django_auth_ldap.backend.LDAPBackend',
	'django.contrib.auth.backends.ModelBackend',
)

ALLOWED_HOSTS = [ '.goo.im' ]

# LDAP Settings

AUTH_LDAP_SERVER_URI = "ldap://10.0.0.5"
AUTH_LDAP_BIND_DN = "cn=admin, dc=goo, dc=im"
AUTH_LDAP_BIND_PASSWORD = "oxYTznRb14ZxbXpquukNDqTq"
AUTH_LDAP_USER_SEARCH = LDAPSearchUnion(
	LDAPSearch("ou=admins,dc=goo,dc=im", ldap.SCOPE_SUBTREE, "(uid=%(user)s)"),
	LDAPSearch("ou=devs,dc=goo,dc=im", ldap.SCOPE_SUBTREE, "(uid=%(user)s)"),
	LDAPSearch("ou=builders,dc=goo,dc=im", ldap.SCOPE_SUBTREE, "(uid=%(user)s)"),
)

# Paypal Settings

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_SUBJECT_PREFIX = '[Goo.im] '
EMAIL_HOST_USER = "contact@snipanet.com"
EMAIL_HOST_PASSWORD = "wtfhax!!"

#WSGI_APPLICATION = 'goo.wsgi.application'

STATIC_URL = 'http://static.junaos.com/'