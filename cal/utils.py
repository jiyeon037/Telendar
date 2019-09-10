from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event

class Calendar(HTMLCalendar):
   def __init__(self, year=None, month=None):
      self.year = year
      self.month = month
      super(Calendar, self).__init__()

   # formats a day as a td
   # filter events by day
   def formatday(self, day, events):
      events_per_day = events.filter(start_time__day=day)
      d = ''
      for event in events_per_day:
         d += f'<li"> {event.get_html_url} </li">'

      if day != 0:
         return f"<td><span class='date'>{day}</span><ul style='list-style:none; padding-left:0px;'> {d} </ul></td>"
      return '<td></td>'

   # formats a week as a tr
   def formatweek(self, theweek, events):
      week = ''
      for d, weekday in theweek:
         week += self.formatday(d, events)
      return f'<tr> {week} </tr>'

   # formats a month as a table
   # filter events by year and month
   def formatmonth(self, withyear=True):
      events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)
      cal = f'<div class="monthYear">\n'
      cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
      cal += f'</div>\n'
      cal += f'</div>\n'
      cal += f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
      cal += f'{self.formatweekheader()}\n'
      for week in self.monthdays2calendar(self.year, self.month):
         cal += f'{self.formatweek(week, events)}\n'
      return cal






class EvnetCalendar(HTMLCalendar):
   def __init__(self, year=None, month=None):
      self.year = year
      self.month = month
      super(EvnetCalendar, self).__init__()

   def formatday(self, day, events):
      events_per_day = events.filter(start_time__day=day)
      d = ''
      for event in events_per_day:
         d += f'<div style="visibility: hidden; position: absolute; width: 0px; height: 0px;">'
         d += f'<svg xmlns="http://www.w3.org/2000/svg">'
         d += f'<symbol viewBox="0 0 24 24" id="expand-more">'
         d += f'<path d="M16.59 8.59L12 13.17 7.41 8.59 6 10l6 6 6-6z" />'
         d += f' <path d="M0 0h24v24H0z" fill="none" />'
         d += f'</symbol>'
         d += f'<symbol viewBox="0 0 24 24" id="close">'
         d += f'<path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z" />'
         d += f'<path d="M0 0h24v24H0z" fill="none" />'
         d += f'</symbol>'
         d += f'</svg>'
         d += f'</div>'
         d += f'<details>'
         d += f'<summary>'
         d += f'<div class="EvnetDayTitle"> {event.get_html_event_url} </div>'
         d += f'<svg class="control-icon control-icon-expand" width="24" height="24" role="presentation"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#expand-more" /></svg>'
         d += f'<svglass c="control-icon control-icon-close" width="24" height="24" role="presentation"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#close" /></svg>'
         d += f'</summary>'
         d += f'<div class="EventTime">{event.StartTime()}-{event.EndTime()}</div>'
         d += f'<div class="EventDayContents">{event.summary()} </div>'
         d += f'</details>'
         

      if day != 0:
         if d != '':
            return f"<div class='Event'><div class='EventDay'>Day {day}</div>{d}</div>"
      return f' '

   # formats a week as a tr
   def formatweek(self, theweek, events):
      week = ''
      for d, weekday in theweek:
         week += self.formatday(d, events)
      return f'{week}'

   # formats a month as a table
   # filter events by year and month
   def formatmonth(self, withyear=True):
      events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)
      cal = f'<div class="monthYear">\n'
      cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
      cal += f'</div>\n</>'
      cal += f'</div>\n</>'
      cal += f'<div class="EventCalendar">\n'
      for week in self.monthdays2calendar(self.year, self.month):
         cal += f'{self.formatweek(week, events)}\n'
      cal +=f'</div>'
      return cal