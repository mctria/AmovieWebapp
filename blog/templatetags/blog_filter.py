from django import template

register  = template.Library()

@register.filter(name='div')
def div(value,args):
    try:
        return int(int(value)/int(args))
    except (ValueError, ZeroDivisionError):
        return None
    