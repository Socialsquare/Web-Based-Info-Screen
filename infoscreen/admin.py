from django.contrib import admin
from infoscreen.models import Slide, Screen

class SlideAdmin(admin.ModelAdmin):
    pass

class ScreenAdmin(admin.ModelAdmin):
    pass

admin.site.register(Slide, SlideAdmin)
admin.site.register(Screen, ScreenAdmin)
