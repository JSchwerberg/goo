from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm
from fabric.contrib import project

# RSync Settings

env.hosts = ['junaos.com']
env.key_file = ['/home/django/.ssh/id_rsa']
env.user = 'goostatic'
env.local_static_root = '/home/django/goo/django/static/'
env.remote_static_root = '/var/www/goostatic'

def deploy_static():
    local('python manage.py collectstatic --settings=goo_new.settings.production')
    project.rsync_project(
        remote_dir = env.remote_static_root,
        local_dir = env.local_static_root,
        delete = True
    )


