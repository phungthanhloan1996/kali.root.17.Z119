from django import template

register = template.Library()

@register.filter
def dict_get(dictionary, key):
    """Truy cập một giá trị trong dictionary bằng key, xử lý khi dictionary hoặc key không hợp lệ."""
    if dictionary is not None:
        return dictionary.get(key)
    return None


