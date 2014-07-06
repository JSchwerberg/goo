from django.conf.urls import patterns, include, url
from files import views

urlpatterns = patterns('',
    url(r'^(?P<cur_path>.*?)/$', views.file_list),
    url(r'^$', views.file_list, name='developers'),
)
