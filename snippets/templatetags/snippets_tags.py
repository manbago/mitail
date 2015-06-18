from django import template
from snippets.models import *
from tail.models import *

register = template.Library()

...

# Advert snippets
@register.inclusion_tag('blog/templates/blog/blog_page.html', takes_context=True)
def adverts(context):
  return {
    'adverts': Advert.objects.all(),
    'request': context['request'],
  }