from django import template

register = template.Library()

@register.filter
def int_dot_format(value):
    try:
        value = int(value)
        return f"{value:,}".replace(",", ".")
    except (ValueError, TypeError):
        return "0"
