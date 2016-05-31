from copy import copy
from django import template
from django.template import loader

register = template.Library()

@register.simple_tag(takes_context=True)
def render_page(context, page):
    tpl = page.get_template()
    request = context['request']
    t = loader.get_template(tpl)
    c = copy(context)
    r = copy(request)
    c['request'] = r
    setattr(r, 'current_page', page)

    return t.render(c)
