from django import template

register = template.Library()

@register.filter
def dict_get(d, key):
    if isinstance(d, dict):
        return d.get(key, '')
    return ''

@register.filter
def count_symbol(attendance_dict, symbol):
    return sum(1 for v in attendance_dict.values() if v == symbol)

@register.filter
def count_other_symbols(attendance_dict, exclude_symbols):
    excluded = exclude_symbols.split(',')
    return sum(1 for v in attendance_dict.values() if v not in excluded)

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key, '')