from django.shortcuts import render
from location_booking.models import Location
from datetime import datetime
from dateutil.tz import tzlocal

def display_location(request, location_id):
	location = Location.objects.get(pk=location_id)
	events_today = location.events_today()
	if len(events_today['allday_events']) > 0:
		is_occupied = True
		minutes_left = None
	else:
		time_left = []
		now = datetime.now( tzlocal() )
		is_occupied = False # Until anything else is shown.
		for event in events_today['regular_events']:
			if event['dtstart'].dt <= now and event['dtend'].dt >= now:
				is_occupied = True
			if event['dtstart'].dt > now:
				time_left.append( event['dtstart'].dt - now )
			if event['dtend'].dt > now:
				time_left.append( event['dtend'].dt - now )
		# Minutes left until the current event ends or a new event starts.
		time_left = min(time_left)
		minutes_left = int(round(time_left.seconds / 60))
	context = {
		'location': location,
		'allday_events': events_today['allday_events'],
		'regular_events': events_today['regular_events'],
		'is_occupied': is_occupied,
		'minutes_left': minutes_left
	}
	return render(request, 'location_booking/display_location.html', context)