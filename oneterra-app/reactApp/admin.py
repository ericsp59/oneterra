from ctypes import Union
from typing import Any, Callable, Optional, Sequence
from django.contrib import admin
from .models import AppSettings

# Register your models here.

class AppSettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'description')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'title', 'description')
    list_editable = ('title', 'description')
    list_filter = ('name', 'title', 'description')

admin.site.register(AppSettings, AppSettingsAdmin)    