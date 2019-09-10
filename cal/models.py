from django.db import models
from django.urls import reverse
from accounts.models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        color="green"
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}" style="color: {color}"> {self.title} </a>'
    @property
    def get_html_event_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
    
    def __str__(self):
        return self.title
    def summary(self):
        return self.description[:100]
    def StartTime(self):
        return '%s' % self.start_time.strftime('%Y/%d/%m/%H:%M')
    def EndTime(self):
        return '%s' % self.end_time.strftime('%Y/%d/%m/%H:%M')


class Theme(models.Model):
    theme_seq = models.IntegerField()
    theme_color = models.TextField()
    theme_content = models.TextField()

    def __str__(self):
        return self.theme_content


class User_Theme(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    theme_seq = models.ForeignKey(Theme, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.user_id, self.theme_seq)


class Schedule(models.Model):
    sche_title = models.TextField()
    theme_seq = models.ForeignKey(Theme, on_delete=models.CASCADE)
    sche_date = models.DateField()
    sche_content = models.TextField()

    def __str__(self):
        return self.sche_title


class Sche_Time(models.Model):
    sche_title = models.OneToOneField(Schedule, on_delete=models.CASCADE) # 1:1
    sche_fromTime = models.TimeField()
    sche_endTime = models.TimeField()

    # def __str__(self):
    #     return self.sche_title