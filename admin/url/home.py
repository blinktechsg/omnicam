from django.conf.urls import url
from admin.views import home as views


urlpatterns = ([
    url(r'^$', views.HomeListView.as_view(), name='list'),
    url(r'^create/$', views.HomeCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.HomeUpdateView.as_view(), name='update'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.HomeDetailView.as_view(), name='detail'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.HomeDeleteView.as_view(), name='delete'),
])
