from django.contrib import admin
from location_booking.models import Calendar, Location

class CalendarAdmin(admin.ModelAdmin):
	pass

class LocationAdmin(admin.ModelAdmin):
	pass

admin.site.register(Calendar, CalendarAdmin)
admin.site.register(Location, LocationAdmin)
