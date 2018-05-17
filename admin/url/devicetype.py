from django.conf.urls import url
from admin.views import devicetype as views


urlpatterns = ([
    url(r'^$', views.DeviceTypeListView.as_view(), name='list'),
    url(r'^create/$', views.DeviceTypeCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.DeviceTypeUpdateView.as_view(), name='update'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.DeviceTypeDetailView.as_view(), name='detail'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.DeviceTypeDeleteView.as_view(), name='delete'),
])
