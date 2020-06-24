from django import template
register = template.Library()

@register.filter
def my_filter(v1,v2):
    return v1

