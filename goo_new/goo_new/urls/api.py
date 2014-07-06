from django.conf.urls import patterns, include, url


urlpatterns =  patterns('',
    # url(r'^oauth2/' include('provider.oauth2.urls', namespace = 'oauth2')),
    # url(r'^$', include('api.urls', namespace='api'))
    # url(r'^files/', 'api.views.file_list', name='file_list'),
    url(r'^files/dev/(?P<dev>\w+)/$', 'api.views.developer_file_list', name='dev_file_list'),
#   url(r'^files/(?P<pk>\d+)/$', 'api.views.file_detail', name='file_detail'),
    url(r'^files/devs/(?P<path>.*)', 'api.views.file_detail', name='file_detail'),
    url(r'^files/', 'api.views.file_list', name='file_list'),
    url(r'^admin/devs/(?P<path>\w+)/$', 'api.views.developer_info', name='developer_info'),
    url(r'^admin/ics/$', 'api.views.latest_ics', name='latest_ics'),
    url(r'^admin/jb/$', 'api.views.latest_jb', name='latest_jb')
)
