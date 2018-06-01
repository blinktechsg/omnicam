from django.conf.urls import url, include
from django.conf import settings
from django.views.static import serve

from admin.views.admins import Homepage

urlpatterns = [
    url(r'^$', Homepage.as_view(), name='index'),
    url(r'^wattsense-admin/', include('admin.urls', namespace='admin')),
    url(r'^api/v1/', include('api.urls', namespace='api')),
    url(r'^media/(?P<path>.*)$', serve, dict(document_root=settings.MEDIA_ROOT)),
    url(r'^static/(?P<path>.*)$', serve, dict(document_root=settings.STATIC_ROOT)),
    url(r'^elements/(?P<path>.*)$', serve, dict(document_root=settings.COMPONENT_ROOT)),
    url(r'^.well-known/(?P<path>.*)$', serve, {'document_root': '/var/www/html/blink/.well-known/'}),
    url(r'^.well-known/acme-challenge/(?P<path>.*)$', serve,
        {'document_root': '/var/www/html/blink/.well-known/acme-challenge/'}),
]
