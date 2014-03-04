from django.db import models

class Slide(models.Model):
    title = models.CharField(max_length=256)
    exposure_time = models.PositiveIntegerField()
    priority = models.PositiveIntegerField()
    def __str__(self):
        return '"%s" [%d seconds exposure time / prio. %d]' % ( self.title, self.exposure_time, self.priority)
    class Meta:
        ordering = ['priority', 'id']

class URLSlide(Slide):
    url = models.CharField(max_length=1024)
    def __str__(self):
        return 'URLSlide %s' % ( super(URLSlide, self).__str__() )

class HTMLSlide(Slide):
    content = models.TextField()
    background_color = models.CharField(max_length=20, blank=True)
    def __str__(self):
        return 'HTMLSlide %s' % ( super(HTMLSlide, self).__str__() )

class Screen(models.Model):
    physical_location = models.CharField(max_length=256)
    slides = models.ManyToManyField(Slide)
    def __str__(self):
        return 'Screen [%s]' % self.physical_location
