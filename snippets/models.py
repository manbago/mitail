from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailsnippets.models import register_snippet

...

@register_snippet
class Advert(models.Model):
  url = models.URLField(null=True, blank=True)
  text = models.CharField(max_length=255)

  panels = [
    FieldPanel('url'),
    FieldPanel('text'),
  ]

  def __unicode__(self):
    return self.text