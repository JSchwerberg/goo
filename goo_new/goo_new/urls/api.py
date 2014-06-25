from django.conf.urls import patterns, include, url


urlpatterns =  patterns('',
    # url(r'^oauth2/' include('provider.oauth2.urls', namespace = 'oauth2')),
    url(r'^$', include('api.urls', namespace='api'))
)
