from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
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


def show_post(request, post_id):
    return HttpResponse(f'Post {post_id}')


def show_category(request, cat_id):
    posts = Breeds.objects.filter(category_id=cat_id).all()
    if len(posts) == 0:
        raise Http404()
    cur_breed = Category.objects.get(pk=cat_id)
    context = {
        'title': cur_breed.name,
        'posts': posts,
        'cat_selected': cat_id
    }
    return render(request, 'cats/index.html', context=context)
