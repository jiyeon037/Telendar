from django.db import models
from django.urls import reverse
# Create your models here.


class Calander(models.Model): 
    title = models.CharField(max_length=200)
    seq = models.CharField(max_length=200)
    user_seq = models.CharField(max_length=200)
    user_id = models.CharField(max_length=200)
    
    @property
    
    def __str__(self):
        return self.title
    

class Cal_theme(models.Model):
    username = models.CharField(max_length=200) #username
    theme_title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.username
    

class Theme(models.Model):
    title = models.CharField(max_length=200, primary_key=True)
    color = models.CharField(max_length=200)
    content = models.TextField()
    
    @property
    def get_html_url(self):
        color="green"
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}" style="color: {color}"> {self.title} </a>'

    def __str__(self):
        return self.title
    def summary(self):
        return self.content[:50]


class Event(models.Model):
    title = models.CharField(max_length=200)
    theme_seq = models.CharField(max_length=200)
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
        return self.body[:100]

