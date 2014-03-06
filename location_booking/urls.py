from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^location/(?P<location_id>\d+)/$', 'location_booking.views.display_location', name='display_location')
)
