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
