from django.conf.urls import url
from admin.views import track as views


urlpatterns = ([
    url(r'^(?P<pk>[0-9]+)/$', views.utility_track, name='track'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.TrackDetailView.as_view(), name='detail'),
    url(r'^chart/(?P<pk>[0-9]+)/$', views.home_track_chart, name='chart'),
])
