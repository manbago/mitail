from django.contrib import admin

# Register your models here.

from .models import MusicianPage, AlbumPage

admin.site.register(MusicianPage)
admin.site.register(AlbumPage)
