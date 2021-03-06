from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import RedirectView
from django.conf.urls import patterns, include, url
from blog.views import IndexView
from files.views import gapps_list, gapps_download, file_search_result_list
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'goo_new.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^confirmation', RedirectView.as_view(url=reverse_lazy('index'), permanent=False)),
    url(r'^sponsor/', include('sponsor.urls')),    
    url(r'^devs/', include('files.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^gapps/$', gapps_list, name='gapps'),
    url(r'^gapps/(?P<path>.*?)/$', gapps_download, name='gapps_download'),
    url(r'^search/', file_search_result_list, name='file_search'),
)
