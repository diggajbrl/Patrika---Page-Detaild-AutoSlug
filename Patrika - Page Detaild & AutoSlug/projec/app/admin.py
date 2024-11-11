from django.contrib import admin
from app.models import *

# Register your models here.

class appAdmin (admin.ModelAdmin):
    list_display = ('news_topic', 'news_desc')
admin.site.register(News, appAdmin)