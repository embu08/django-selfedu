from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import *


def index(request):
    posts = Breeds.objects.all()
    context = {
        'title': 'Breeds',
        'posts': posts,
        'cat_selected': 0
    }
    return render(request, 'cats/index.html', context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound(
        f'<h1>requested page is not found, please enter correct address or visit another page</h1>'
        '<a href="{% url "home" %}">home</a>'
        f'<p>cat</p>')


def about(request):
    context = {
        'title': 'About site',
    }
    return render(request, 'cats/about.html', context=context)


def add(request):
    return HttpResponse('add')


def contact(request):
    return HttpResponse('contact')


def login(request):
    return HttpResponse('login')


def show_post(request, post_slug):
    post = get_object_or_404(Breeds, slug=post_slug)
    context = {'title': post.title,
               'post': post,
               'cat_selected': post.category_id}

    return render(request, 'cats/post.html', context=context)


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Breeds.objects.filter(category=category.id).all()
    context = {
        'title': category.name,
        'posts': posts,
        'cat_selected': category.id
    }
    return render(request, 'cats/index.html', context=context)
