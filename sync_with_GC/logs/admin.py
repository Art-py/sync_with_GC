from django.contrib import admin
from .models import LogEntry


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'level', 'message', 'logger')
    search_fields = ('message', 'level', 'logger')
    list_filter = ('level',)
