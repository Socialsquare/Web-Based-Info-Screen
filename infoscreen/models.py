from django.db import models

class Slide(models.Model):
    url = models.CharField(max_length=256)
    delay = models.PositiveIntegerField()
    priority = models.PositiveIntegerField()
    def __str__(self):
        return 'Slide [%s for %d seconds / prio. %d]' % ( self.url, self.delay, self.priority)

class Screen(models.Model):
    physical_location = models.CharField(max_length=256)
    slides = models.ManyToManyField(Slide)
    def __str__(self):
        return 'Screen [%s]' % self.physical_location
