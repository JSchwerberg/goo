from django.conf.urls import patterns, include, url
from .views import login_view, logout_view, payment, authkey_view, complete_signup, password_reset_request_view, password_reset_view

urlpatterns = patterns('',
    url(r'^login/', login_view, name="sponsor_login"),
    url(r'^logout/', logout_view, name="sponsor_logout"),
    url(r'^signup/', payment, name="sponsor_signup"),
    url(r'^complete/', complete_signup, name="sponsor_signup2"),
    url(r'^b57acd4931b1bae8db9cae5c798ff159/', include('paypal.standard.ipn.urls')),
    url(r'^auth/', authkey_view, name="sponsor_authkey"),
    url(r'^reset/', password_reset_request_view, name="sponsor_reset"),
    url(r'^password/', password_reset_view, name="sponsor_password"),
)
