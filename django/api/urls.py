from django.conf.urls import patterns. url

from api import views

urlpatterns = patterns('',
	url(r'^files/', 'api.views.file_list', name='file_list'),
	)