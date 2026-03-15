from django import template

register = template.Library()

@register.filter
def dict_get(d, key):
    return d.get(key, 0)

@register.filter
def int_dot_format(value):
    """Định dạng số có dấu chấm phần nghìn: 1000000 -> 1.000.000"""
    try:
        return "{:,.0f}".format(float(value)).replace(",", ".")
    except (ValueError, TypeError):
        return value
from django import template
from django.contrib.humanize.templatetags.humanize import intcomma as django_intcomma

register = template.Library()

@register.filter
def intcomma(value):
    try:
        return django_intcomma(int(value))
    except:
        return value
