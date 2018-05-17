from django.conf.urls import url
from admin.views import activity as views


urlpatterns = ([
    url(r'^$', views.get_activity, name='get-activity'),
])
