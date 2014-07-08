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
        'HOST': 'intlb.goo.im',
        'PORT': '3306',
    }
}

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
EMAIL_HOST_USER = "support@snipanet.com"
EMAIL_HOST_PASSWORD = "eU1kct%%Wpn%&^r"

#WSGI_APPLICATION = 'goo.wsgi.application'

STATIC_URL = 'https://d1vynbeceyk9dd.cloudfront.net/'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'intlb.goo.im:11211',
    }
}

SESSION_COOKIE_AGE = 4838400
SESSION_COOKIE_SECURE = True
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

GAPPS_KEY = "93heq298unrf312890h"

CSRF_COOKIE_DOMAIN = ".goo.im"
CSRF_COOKIE_SECURE = True
