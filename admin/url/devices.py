from django.conf.urls import url
from admin.views import devices as views


urlpatterns = ([
    url(r'^$', views.DeviceListView.as_view(), name='list'),
    url(r'^create/$', views.DeviceCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.DeviceUpdateView.as_view(), name='update'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.DeviceDetailView.as_view(), name='detail'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.DeviceDeleteView.as_view(), name='delete'),

])


urlpatterns2 = ([
    url(r'^$', views.DeviceStatusListView.as_view(), name='list'),
    url(r'^create/$', views.DeviceStatusCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.DeviceStatusUpdateView.as_view(), name='update'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.DeviceStatusDetailView.as_view(), name='detail'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.DeviceStatusDeleteView.as_view(), name='delete'),

])