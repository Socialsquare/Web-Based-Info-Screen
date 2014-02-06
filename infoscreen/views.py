from django.shortcuts import render
from infoscreen.models import Slide, Screen
from django.core import serializers

def display_screen(request, screen_id):
    slides = Slide.objects.filter(screen=screen_id)
    context = {
    	'slides_json': serializers.serialize('json', slides)
    }
    return render(request, 'infoscreen/display_screen.html', context)


def list_screens(request):
    screens = Screen.objects.all()
    context = {
    	'screens': screens
    }
    return render(request, 'infoscreen/list_screens.html', context)
