from django.db import models
import requests, icalendar, re
from datetime import datetime, date
from dateutil.tz import tzlocal

def localize_timezones(event):
    '''Makes sure all date and datetimes are in the local timezone.'''
    for field_name, field_value in event.items():
        if isinstance(field_value, icalendar.prop.vDDDTypes):
            # Is this infact a datetime?
            if isinstance(field_value.dt, datetime):
                event[field_name].dt = field_value.dt.astimezone( tzlocal() )
    return event

def event_compare(event_a, event_b):
	return cmp(event_a.get('DTSTART').dt > event_b.get('DTSTART').dt)

class Calendar(models.Model):
    ical_url = models.CharField(max_length=1024)
    calendar = None
    def __str__(self):
        return 'Calendar (%s)' % ( self.ical_url )
    def load(self):
        response = requests.get(self.ical_url)
        self.calendar = icalendar.Calendar.from_ical(response.text)
        name = self.calendar.get('X-WR-CALNAME')
        description = self.calendar.get('X-WR-CALDESC')
        if name and description:
            print "Loaded calendar: '%s' (%s)." % (name, description)
        elif name:
            print "Loaded calendar: '%s'." % (name)
        else:
            print "Loaded calendar!"
    def all_events(self):
        self.load()
        result = []
        for event in self.calendar.walk("VEVENT"):
            event = localize_timezones(event)
            result.append(event)
        return result
    def events_today(self):
        events = self.all_events()
        result = []
        now = datetime.now(tzlocal())
        this_morning = now.replace(hour=0, minute=0)
        this_midnight = now.replace(hour=23, minute=59)
        for event in events:
        	start = event.get('DTSTART').dt
        	if type(start) == date:
        		if this_morning.date() == start:
        			result.append(event)
        	elif start > this_morning and start < this_midnight:
        		result.append(event)
        return result

class Location(models.Model):
    calendar = models.ForeignKey('Calendar')
    title = models.CharField(max_length=256)
    location_regexp = models.CharField(max_length=256)
    def __str__(self):
        return 'Location (%s in %s)' % ( self.location_regexp, self.calendar.ical_url )

    def events_today(self):
        future_calendar_events = self.calendar.events_today()
        result = {
        	'allday_events': [],
        	'regular_events': []
        }
        for event in future_calendar_events:
        	location = event.get('LOCATION')
        	if location and re.search(self.location_regexp, location, flags=re.IGNORECASE):
        		event_dict = dict()
        		for k,v in event.items():
        			k = k.lower().replace('-', '_')
        			event_dict[k] = v
        		if type(event.get('DTSTART').dt) == date:
        			result['allday_events'].append(event_dict)
        		else:
        			result['regular_events'].append(event_dict)
       	# Sort based on start-time.
       	result['regular_events'] = sorted(result['regular_events'], event_compare)
        return result