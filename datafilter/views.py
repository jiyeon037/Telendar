
from django.shortcuts import render, get_object_or_404
from .models import Theme, Cal_theme, Event
from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse
from accounts.models import Profile

# Create your views here.


def home(request):
    return render(request, 'home.html')

def kategorie(request):
    themes = Theme.objects.all()
    username = request.user.username
    cal_themes = Cal_theme.objects.filter(username = username)
    event_results = Event.objects.none()
    for cal_theme in cal_themes:
        event_results |= Event.objects.filter(theme_seq = cal_theme.theme_title)
    #event_results = Event.objects.filter(theme_seq = '야구')
    #Room.objects.select_related('house').filter(house__street=xyz) # forign key 사용시
    return render(request, 'kategorie.html', {'themes':themes,'cal_themes':cal_themes, 'event_results':event_results})

def theme_detail(request, theme_title):
    theme_detail = get_object_or_404(Theme, pk=theme_title)
    return render(request, 'theme_detail.html', {'theme': theme_detail})

def theme_add(request, theme_title):        #입력받은 내용을 데이터베이스에 넣어주는 함수
    #if request.user.is_authenticated():
    username = request.user.username
    theme_name = get_object_or_404(Theme, pk=theme_title)
    cal_theme = Cal_theme()
    cal_theme.username = username
    cal_theme.theme_title = theme_name
    cal_theme.save()
    return HttpResponseRedirect(reverse('data_kategorie'))