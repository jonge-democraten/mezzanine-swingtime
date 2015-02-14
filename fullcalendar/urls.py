from django.conf.urls import patterns, url
from fullcalendar import views

urlpatterns = patterns('',
    url(
        r'^(?:calendar/)?$',
        views.CalendarView.as_view(),
        name='fullcalendar-calendar'
    ),

    url(
        r'^calendar.json$',
        views.CalendarJSONView.as_view(),
        name='fullcalendar-calendar-json'
    ),

    url(
        r'^calendar/(?P<year>\d{4})/$',
        views.CalendarView.as_view(),
        name='fullcalendar-yearly-view'
    ),

    url(
        r'^calendar/(?P<year>\d{4})/(?P<month>0?[1-9]|1[012])/$',
        views.CalendarView.as_view(),
        name='fullcalendar-monthly-view'
    ),

    url(
        r'^agenda/$',
        views.AgendaView.as_view(),
        name='fullcalendar-agenda'
    ),

    url(
        r'^event/(?P<id>\d+)/$',
        views.EventView.as_view(),
        name='fullcalendar-event'
    ),
)