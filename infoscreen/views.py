from django.shortcuts import render
from infoscreen.models import URLSlide, HTMLSlide, Screen
from django.core import serializers

def display_screen(request, screen_id):
    #slides = Slide.objects.filter(screen=screen_id)
    url_slides = URLSlide.objects.filter(screen=screen_id).order_by('priority', 'id')
    html_slides = HTMLSlide.objects.filter(screen=screen_id).order_by('priority', 'id')

    url_slides = list(url_slides)
    html_slides = list(html_slides)
    slides = url_slides + html_slides
    slides = sorted(slides, lambda a,b: cmp(a.priority, b.priority))

    context = {
    	'slides_json': serializers.serialize('json', slides)
    }
    return render(request, 'infoscreen/display_screen.html', context)

def display_htmlslide(request, slide_id):
    slide = HTMLSlide.objects.get(pk=slide_id)
    context = {
        'slide': slide
    }
    return render(request, 'infoscreen/display_htmlslide.html', context)

def list_screens(request):
    screens = Screen.objects.all()
    context = {
    	'screens': screens
    }
    return render(request, 'infoscreen/list_screens.html', context)
