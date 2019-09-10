from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'cal'
urlpatterns = [
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    url(r'^event/new/$', views.event, name='event_new'),
	url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
    url(r'^eventcalendar/$', views.EventCalendarView.as_view(), name="event_calendar"),
    path('theme/', views.theme, name='theme'),
    path('theme/<str:theme_title>/', views.theme_detail, name="theme_detail"),
    path('theme_add/<str:theme_title>/', views.theme_add, name ="theme_add"),
]
