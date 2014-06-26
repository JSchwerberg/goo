from django.conf.urls import patterns, include, url


urlpatterns =  patterns('',
    # url(r'^oauth2/' include('provider.oauth2.urls', namespace = 'oauth2')),
    # url(r'^$', include('api.urls', namespace='api'))
    # url(r'^files/', 'api.views.file_list', name='file_list'),
    url(r'^files/(?P<pk>\d+)/$', 'api.views.file_detail', name='file_detail'),
    url(r'^files/', 'api.views.file_list', name='file_list'),

)
