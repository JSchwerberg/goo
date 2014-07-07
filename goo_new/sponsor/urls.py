from django.conf.urls import patterns, include, url
from .views import login_view, logout_view

urlpatterns = patterns('',
    url(r'^login/', login_view, name="sponsor_login"),
    url(r'^logout/', logout_view, name="sponsor_logout"),
)
