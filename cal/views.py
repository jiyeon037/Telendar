from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
import calendar
from django.contrib.auth.models import User
from django.template import RequestContext
from .models import *
from .utils import Calendar
from .utils import EvnetCalendar
from .forms import EventForm



class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        context['activate'] = 'cal:calendar'
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    events = get_object_or_404(Event, pk=event_id)
    #events =Event.objects.filter(description =2)
    return render(request, 'cal/event.html', {'events': events})

def eventcalendar(request):
    events = Event.objects
    #events =Event.objects.filter(description =2)
    return render(request, 'cal/eventcalendar.html', {'events': events})



class EventCalendarView(generic.ListView):
    model = Event
    template_name = 'cal/eventcalendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = EvnetCalendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['EvnetCalendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_eventmonth(d)
        context['next_month'] = next_evnetmonth(d)
        context['activate'] = 'cal:event_calendar'
        return context

def prev_eventmonth(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_evnetmonth(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def theme(request):
    themes = Theme.objects.all()
    username = request.user.username
    ui = User.objects.get(username = username)
    user_themes = User_Theme.objects.filter(user_id = ui).distinct()
    event_results = Event.objects.none()
    for user_theme in user_themes:
        event_results |= Event.objects.filter(description = user_theme.theme_seq.theme_seq)
    ## ui = User.objects.get(username = username)
    ## user_themes = User_Theme.objects.filter(user_id = ui)
    #cal_themes = Cal_theme.objects.filter(username = username)
    ## event_results = Event.objects.none()
    #for cal_theme in cal_themes:
    #    event_results |= Event.objects.filter(theme_seq = cal_theme.theme_title)
    #event_results = Event.objects.filter(theme_seq = '야구')
    #Room.objects.select_related('house').filter(house__street=xyz) # forign key 사용시
    #return render(request, 'kategorie.html', {'themes':themes,'cal_themes':cal_themes, 'event_results':event_results})
    #return render(request, 'cal/theme.html', {'themes':themes, 'user_themes':user_themes})
    return render(request, 'cal/theme.html', {'themes':themes, 'user_themes':user_themes, 'event_results':event_results})

def theme_detail(request, theme_title):
    #theme_detail = get_object_or_404(Theme, pk=theme_title)
    theme_detail = Theme.objects.get(theme_seq = theme_title)
    return render(request, 'cal/theme_detail.html', {'theme': theme_detail})

def theme_add(request, theme_title):        #입력받은 내용을 데이터베이스에 넣어주는 함수
    #if request.user.is_authenticated():
    username = request.user.username
    theme_name = get_object_or_404(Theme, theme_seq=theme_title)
    User_Themes = User_Theme()
    ui = User.objects.get(username = username)
    User_Themes.user_id = ui
    fkt = Theme.objects.get(theme_seq=theme_title)
    User_Themes.theme_seq = fkt
    User_Themes.save()
    return HttpResponseRedirect(reverse('cal:theme'))