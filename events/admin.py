from django.contrib import admin

from .models import Event, EventCategory

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'eventtype', 'venue', 'date', 'scheduler', 'status')
    list_filter = ('status',)
    search_fields = ['name', 'about']

class EventCategoryAdmin(admin.ModelAdmin):
    fields = ['name']

admin.site.register(Event, EventAdmin)
admin.site.register(EventCategory, EventCategoryAdmin)
