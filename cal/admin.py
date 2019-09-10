from django.contrib import admin
from cal.models import Event
from cal.models import Theme
from cal.models import Schedule
from cal.models import *
from accounts.models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(Event)
admin.site.register(Theme)
admin.site.register(User_Theme)
admin.site.register(Schedule)
admin.site.register(Sche_Time)