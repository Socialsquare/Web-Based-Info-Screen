from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^(?P<screen_id>\d)/$', 'infoscreen.views.display_screen', name='display_screen'),
	url(r'^$', 'infoscreen.views.list_screens', name='list_screens')
)
