from django.db.models import Count

from .models import *

menu = [{'title': 'Main', 'url_name': 'home'},
        {'title': 'Add page', 'url_name': 'add'},
        {'title': 'About', 'url_name': 'about'},
        {'title': 'Contact', 'url_name': 'contact'},
        {'title': 'Admin', 'url_name': 'admin'},
        {'title': 'Login', 'url_name': 'login'},
        ]


class DataMixin:
    paginate_by = 4

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('breeds'))
        context['cats'] = cats

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu

        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
