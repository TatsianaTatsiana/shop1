from django import template

register = template.Library()


@register.inclusion_tag("add_to_cart_form.html")
def add_to_cart_form(item):
    return {'item': item}
