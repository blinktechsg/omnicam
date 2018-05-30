from django.conf.urls import url
from admin.views import utilitys as views


urlpatterns = ([
    url(r'^track/(?P<pk>[0-9]+)/$', views.utility_track, name='track'),
    url(r'^track/de(?P<pk>[0-9]+)/$', views.utility_track, name='track'),

])
