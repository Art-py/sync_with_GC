from django.contrib import admin
from .models import Company, Hall, Event


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'google_token')


@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company', 'google_calendar_id')
    list_filter = ('company',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'google_id', 'company', 'hall', 'date_start', 'date_end', 'error')
    list_filter = ('company', 'hall', 'date_start')
