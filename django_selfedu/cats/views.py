from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Main page of the app "Cats"')


def categories(request):
    return HttpResponse('<h1>Cats by categories</h1>')
