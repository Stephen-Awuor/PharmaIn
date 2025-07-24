# templatetags/math_filters.py
from django import template
register = template.Library()

@register.filter
def multiply(qty, price):
    return qty * price
