"""
Django settings for goo_new project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from unipath import Path 
import os
BASE_DIR = Path(__file__).ancestor(3)
MEDIA_ROOT = BASE_DIR.child("media")
STATIC_ROOT = BASE_DIR.child("static")
STATICFILES_DIRS = (
    BASE_DIR.child("assets"),
)
TEMPLATE_DIRS = (
    BASE_DIR.child("templates"),
)

ALLOWED_HOSTS = []

SITE_ID = 7

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'raven.contrib.django.raven_compat',
    'api',
    'south',
    'configuration',
    #'sponsor',
    'developer',
    'recovery',
    'files',
    'rest_framework',
    'subdomains',
    'paypal.standard.ipn',
    'gunicorn',
    'blog',    
    'sponsor',
    'qrcode',
    'corsheaders',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'subdomains.middleware.SubdomainURLRoutingMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
)

ROOT_URLCONF = 'goo_new.urls.account'

SUBDOMAIN_URLCONFS = {
    None: 'goo_new.urls.frontend', # no subdomain, e.g. 'goo.im'
    'www': 'goo_new.urls.frontend',
    'dev': 'goo_new.urls.frontend',
    'api': 'goo_new.urls.api',
    'admin': 'goo_new.urls.admin',
}

#WSGI_APPLICATION = 'goo_new.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

REST_FRAMEWORK = {
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',

    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),

    'DEFAULT_RENDERER_CLASSES': (
        'drf_toolbox.renderers.json.JSONRenderer',
    ),
    
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'api.authentication.TokenAuthentication',
    )

}

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "configuration.context_processors.init_site_settings",
)

DATETIME_INPUT_FORMATS = (
    '%Y-%m-%d %H:%M:%S',     # '2006-10-25 14:30:59'
    '%Y-%m-%d %H:%M:%S.%f',  # '2006-10-25 14:30:59.000200'
    '%Y-%m-%d %H:%M',        # '2006-10-25 14:30'
    '%Y-%m-%d',              # '2006-10-25'
    '%m/%d/%Y %H:%M:%S',     # '10/25/2006 14:30:59'
    '%m/%d/%Y %H:%M:%S.%f',  # '10/25/2006 14:30:59.000200'
    '%m/%d/%Y %H:%M',        # '10/25/2006 14:30'
    '%m/%d/%Y',              # '10/25/2006'
    '%m/%d/%y %H:%M:%S',     # '10/25/06 14:30:59'
    '%m/%d/%y %H:%M:%S.%f',  # '10/25/06 14:30:59.000200'
    '%m/%d/%y %H:%M',        # '10/25/06 14:30'
    '%m/%d/%y',              # '10/25/06'
    '%a, %d %b %Y %H:%M:%S %Z',     # 'Sun, 22 Jan 2014 17:50:02 GMT'
)

RAVEN_CONFIG = {
    # 'dsn': 'https://e0f915efe33441f68cb99c9ba219fecb:3789e8dd63cc48b7bec3b230ace13077@sentry.goo.im/3'
    'dsn': 'https://0769f8c2390542e9935209756ccc6c63:8068726a9c944b86a7faa1f46c8876fc@app.getsentry.com/27189'
}

CORS_ORIGIN_WHITELIST = (
    'd1vynbeceyk9dd.cloudfront.net',
)
