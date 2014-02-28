from django.contrib import admin
from infoscreen.models import URLSlide, HTMLSlide, Screen

class SlideAdmin(admin.ModelAdmin):
	ordering = ['priority', 'id']

class ScreenAdmin(admin.ModelAdmin):
	pass

admin.site.register(URLSlide, SlideAdmin)
admin.site.register(HTMLSlide, SlideAdmin)
admin.site.register(Screen, ScreenAdmin)
