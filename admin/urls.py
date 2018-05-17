from django.conf.urls import url, include
from admin.views.admins import Dashboard
from admin.generic import json_view
from admin.url.projects import urlpatterns as projects
from admin.url.devicetype import urlpatterns as devicetype
from admin.url.home import urlpatterns as home
from admin.url.hardware import urlpatterns as hardware
from admin.url.devices import urlpatterns as devices
from admin.url.devices import urlpatterns2 as devicestatus
from admin.url.activity import urlpatterns as activity


urlpatterns = [
    url(r'^dashboard/$', Dashboard.as_view(), name='dashboard'),
    url(r'^ajax/(?P<page>\S+)/', json_view, name='ajax-list'),
    url(r'^project/', include(projects, namespace='project')),
    url(r'^devicetype/', include(devicetype, namespace='devicetype')),
    url(r'^home/', include(home, namespace='home')),
    url(r'^hardware/', include(hardware, namespace='hardware')),
    url(r'^devices/', include(devices, namespace='devices')),
    url(r'^devicestatus/', include(devicestatus, namespace='devicestatus')),
    url(r'^activity/', include(activity, namespace='activity')),
]
