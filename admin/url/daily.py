from django.conf.urls import url
from admin.views import daily as views


urlpatterns = ([
    url(r'^(?P<pk>[0-9]+)/$', views.utility_daily, name='track'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.DailyDetailView.as_view(), name='detail'),
])
