from typing import Counter
from .models import *


menu = [
    {"title": "О сайте", "url_name": "about"},
    {"title": "Добавить статью", "url_name": "add_page"},
    {"title": "Обратная связь", "url_name": "contact"},
    # {'title': "Войти", 'url_name': 'login'}  # главное меню сайта
]


# class DataMixin:
#     paginate_by = 3

#     def get_user_context(self, **kwargs):
#         context = kwargs
#         cats = Category.objects.all()

#         context['menu'] = menu
#         context['cats'] = cats
#         if 'cat_selected' not in context:
#             context['cat_selected'] = 0
#         return context


class DataMixin:
    paginate_by = 4

    def get_user_context(self, **kwargs):
        context = kwargs

        cats = Category.objects.all()

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context["menu"] = user_menu
        context["cats"] = cats
        if "cat_selected" not in context:
            context["cat_selected"] = 0

        return context
