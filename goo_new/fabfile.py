from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm
from fabric.contrib import project

# RSync Settings

env.roledefs = {
    'web': ['django2.goo.im'],
    'static': ['junaos.com']
}

env.keyfile = '/home/django/.ssh/id_rsa'

def deploy_static():
    env.hosts = ['junaos.com']
    env.user = 'goostatic'
    env.local_static_root = '/home/django/goo/goo_new/static/'
    env.remote_static_root = '/var/www/goostatic'
    local('python manage.py collectstatic --settings=goo_new.settings.production')
    project.rsync_project(
        remote_dir = env.remote_static_root,
        local_dir = env.local_static_root,
        delete = True
    )


def deploy_server():
    env.hosts = ['django2.goo.im']
    env.user = 'django'
    env.local_static_root = '/home/django/goo/goo_new/'
    env.remote_static_root = '/home/django/goo/goo_new/'
    project.rsync_project(
        remote_dir = env.remote_static_root,
        local_dir = env.local_static_root,
        delete = True
    )
