import sys,os
if not '/home/django/goo/goo_new' in sys.path:
    sys.path.insert(1, '/home/django/goo/goo_new')
if not '/home/django/envs/django/lib/python2.7/site-packages/gunicorn' in sys.path:
    sys.path.insert(1, '/home/django/envs/django/lib/python2.7/site-packages/gunicorn')


os.environ["DJANGO_SETTINGS_MODULE"] = "goo_new.settings.production"

def when_ready(server):
    from django.core.management import call_command
    call_command('validate')
