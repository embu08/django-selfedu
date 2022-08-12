from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *

menu = [{'title': 'Main', 'url_name': 'home'},
        {'title': 'Add page', 'url_name': 'add'},
        {'title': 'About', 'url_name': 'about'},
        {'title': 'Contact', 'url_name': 'contact'},
        {'title': 'Login', 'url_name': 'login'},
        ]


def index(request):
    posts = Breeds.objects.all()
    categories = Category.objects.all()
    context = {
        'title': 'Breeds',
        'menu': menu,
        'posts': posts,
        'categories': categories,
        'cat_selected': 0
    }
    return render(request, 'cats/index.html', context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound(
        f'<h1>requested page is not found, please enter correct address or visit another page</h1>'
        f'<a href=''>home</a>'
        f'<p>cat</p>')


def about(request):
    context = {
        'title': 'About site',
        'menu': menu
    }
    return render(request, 'cats/about.html', context=context)


def add(request):
    return HttpResponse('add')


def contact(request):
    return HttpResponse('contact')


def login(request):
    return HttpResponse('login')


def show_post(request, post_id):
    return HttpResponse(f'Post {post_id}')


def show_category(request, cat_id):
    posts = Breeds.objects.filter(category_id=cat_id).all()
    if len(posts) == 0:
        raise Http404()
    categories = Category.objects.all()
    cur_breed = Category.objects.get(pk=cat_id)
    context = {
        'title': cur_breed.name,
        'menu': menu,
        'posts': posts,
        'categories': categories,
        'cat_selected': cat_id
    }
    return render(request, 'cats/index.html', context=context)
