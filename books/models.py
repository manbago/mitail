from django.db import models
from wagtail.wagtailcore.models import Page
# Create your models here.

class MusicianPage(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class AlbumPage(models.Model):
    artist = models.ForeignKey(MusicianPage)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()