""" Import Template to calculate subtotal """

from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ Calculate Subtotal """
    return price * quantity
