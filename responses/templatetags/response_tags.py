from django import template

register = template.Library()


@register.filter
def div(value, arg=5):
    '''
    Divides the value; argument is the divisor.
    Returns empty string on any error.
    '''
    try:
        value = int(value)
        arg = int(arg)
        if arg: return round(value / arg * 100)
    except:
        pass
    return ''
