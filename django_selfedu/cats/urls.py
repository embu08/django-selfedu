from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('add/', add, name='add'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('show_post/<int:post_id>', show_post, name='show_post')
]
