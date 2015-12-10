from django import template
from django.contrib.humanize.templatetags.humanize import intcomma
import decimal
register = template.Library()


def mult(value, arg):
    "Multiplies the arg and the value"
    return intcomma(float(value * arg))
mult.is_safe = False

def percent(value):
    "Turns a float into a percent."
    value = float(value)
    return intcomma(float(value * 100))
percent.is_safe = False

def sub(value, arg):
    "Subtracts the arg from the value"
    return intcomma(int(value) - int(arg))
sub.is_safe = False

def div(value, arg):
    "Divides the value by the arg"
    return round((value / arg),2)
div.is_safe = False

def decimalmult(value, arg):
    return round((value * arg), 2)
decimalmult.is_safe = False

def roundeddecimalmult(value, arg):
    return int((value * arg))
roundeddecimalmult.is_safe = False

register.simple_tag(div)
register.simple_tag(sub)
register.simple_tag(mult)
register.simple_tag(percent)
register.simple_tag(decimalmult)
register.simple_tag(roundeddecimalmult)