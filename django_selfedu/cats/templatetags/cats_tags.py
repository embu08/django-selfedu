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


@register.simple_tag()
def get_menu():
    menu = [{'title': 'Main', 'url_name': 'home'},
            {'title': 'Add page', 'url_name': 'add'},
            {'title': 'About', 'url_name': 'about'},
            {'title': 'Contact', 'url_name': 'contact'},
            {'title': 'Login', 'url_name': 'login'},
            ]
    return menu
