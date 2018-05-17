from django.conf.urls import url, include
from . import views


urlpatterns = ([
    url(r'^add/device/activity/$', views.CreateActivityView.as_view()),
    url(r'^add/device/status/$', views.CreateStatusView.as_view()),
    url(r'^add/device/monthly/$', views.CreateMonthlyView.as_view()),
    url(r'^add/utility/track/$', views.CreateTrackView.as_view()),
    url(r'^add/utility/daily/$', views.CreateDailyView.as_view()),
    url(r'^add/utility/monthly/$', views.CreateUtilityMonthlyView.as_view()),
])
