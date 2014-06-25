from .production import *

DEBUG = True
TEMPLATE_DEBUG = True

INSTALLED_APPS += (
    'debug_toolbar',
)

SECRET_KEY = "08zvpmkdo=^rnid92=+_0*z!r2p^w&cp%94@9uil%wrnl9ztr$"

INTERNAL_IPS = ('70.173.255.59', 
)
