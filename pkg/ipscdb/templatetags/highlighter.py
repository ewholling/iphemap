from django import template
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
import re
register = template.Library()

@register.filter(needs_autoescape=True)
def highlight(string, autoescape=None):
  #s = mark_safe(string
  #              .replace('Increased', '<span class="highlight_red">Increased</span>')
  #              .replace('Decreased', '<span class="highlight_blue">Decreased</span>')
  #              )
  s = mark_safe(
        re.sub('(?i)(increased?)', r'<span class="highlight_red">\1</span>',
        re.sub('(?i)(decreased?)', r'<span class="highlight_blue">\1</span>',
            string)))
  return s

@register.filter(needs_autoescape=True)
def highlight_search(string, query, autoescape=None):
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    if len(query) > 0:
        r = re.compile('({0})'.format(query), re.IGNORECASE)
        return mark_safe(r.sub('<span class="highlight_search">\g<1></span>', string))
    else:
        return mark_safe(string)
