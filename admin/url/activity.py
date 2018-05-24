from django.conf.urls import url
from admin.views import activity as views


urlpatterns = ([
    url(r'^$', views.get_activity, name='get-activity'),
    url(r'^device/$', views.get_home_devices, name='get-device'),
])
