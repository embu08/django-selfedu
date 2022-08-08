from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse('Main page of the app "Cats"')


def categories(request, catid):
    if int(catid) > 100:
        return redirect('home')
    return HttpResponse(f'<h1>Category {catid}</h1>')


def page_not_found(request, exception):
    return HttpResponseNotFound(
        f'<h1>requested page is not found, please enter correct address or visit another page</h1>'
        f'<a href=''>home</a>'
        f'<p>cat</p>')
