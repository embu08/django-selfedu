from django import template
from cats.models import *

register = template.Library()


@register.simple_tag()
def get_categories(fil=None):
    if filter:
        return Category.objects.filter(pk=fil)
    return Category.objects.all()


@register.inclusion_tag('cats/list_categories.html')
def show_categories(sorting=None, cat_selected=0):
    if not sorting:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sorting)

    return {'cats': cats, 'cat_selected': cat_selected}
