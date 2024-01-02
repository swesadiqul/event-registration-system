from django.contrib import admin
from .models import Event, Registration


#Register your models here
class RegistrationInline(admin.TabularInline):
    model = Registration
    extra = 0

class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'time', 'location_name', 'available_slots']
    search_fields = ['title', 'description', 'location_name']
    inlines = [RegistrationInline]

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['user', 'event']
    search_fields = ['user__username', 'event__title']

admin.site.register(Event, EventAdmin)
admin.site.register(Registration, RegistrationAdmin)


# Customize the site header, site title, and index title
admin.site.site_header = 'Event Registration System Administration'
admin.site.site_title = 'Event Registration System Admin'
admin.site.index_title = 'Welcome to the Event Registration System Admin Panel'
