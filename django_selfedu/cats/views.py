from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

menu = ['Main', 'Add', 'Feedback', 'About']
from .models import *


def index(request):
    posts = Cats.objects.all()
    return render(request, 'cats/index.html', {'title': 'Main page', 'menu': menu, 'posts': posts})


def page_not_found(request, exception):
    return HttpResponseNotFound(
        f'<h1>requested page is not found, please enter correct address or visit another page</h1>'
        f'<a href=''>home</a>'
        f'<p>cat</p>')


def about(request):
    return render(request, 'cats/about.html', {'title': 'About site', 'menu': menu})
