from django.conf.urls import url
from admin.views import projects as views


urlpatterns = ([
    url(r'^$', views.ProjectListView.as_view(), name='list'),
    url(r'^create/$', views.ProjectCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.ProjectUpdateView.as_view(), name='update'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.ProjectDetailView.as_view(), name='detail'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.ProjectDeleteView.as_view(), name='delete'),
])
