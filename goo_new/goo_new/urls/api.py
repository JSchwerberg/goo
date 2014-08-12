from django.conf.urls import patterns, include, url


urlpatterns =  patterns('',
    # url(r'^oauth2/' include('provider.oauth2.urls', namespace = 'oauth2')),
    # url(r'^$', include('api.urls', namespace='api'))
    # url(r'^files/', 'api.views.file_list', name='file_list'),
    url(r'^search/(?P<search>.*?)/$', 'api.views.file_search_result_list', name='file_search'),
    url(r'^login/$', 'api.views.login', name='api_login'),
    url(r'^files/$', 'api.views.folder_list', name='root_folder_list'),
    url(r'^files/devs$', 'api.views.folder_list'),
    url(r'^files/devs/$', 'api.views.folder_list'), 
    url(r'^files/dev/(?P<dev>.*?)$', 'api.views.developer_file_list', name='dev_file_list'),
    # url(r'^files/(?P<pk>\d+)/$', 'api.views.file_detail', name='file_detail'),
    url(r'^files/(?P<folder>.*?)$', 'api.views.file_list', name='file_list'),
    # url(r'^files/', 'api.views.file_list', name='file_list'),
    url(r'^install_command/(?P<device>.*?)/$', 'api.views.install_command_view', name='install_command'),
    url(r'^admin/devs/(?P<path>.*?)/$', 'api.views.developer_info', name='developer_info'),
    url(r'^admin/ics/$', 'api.views.latest_ics', name='latest_ics'),
    url(r'^admin/jb/$', 'api.views.latest_jb', name='latest_jb')
    url(r'^admin/delete/(?P<path>.*?)/$', 'api.views.file_delete', name='file_delete')
)
