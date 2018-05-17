from django.conf.urls import url
from admin.views import hardware as views


urlpatterns = ([
    url(r'^$', views.HardwareListView.as_view(), name='list'),
    url(r'^create/$', views.HardwareCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.HardwareUpdateView.as_view(), name='update'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.HardwareDetailView.as_view(), name='detail'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.HardwareDeleteView.as_view(), name='delete'),
])
