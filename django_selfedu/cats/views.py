from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import *
from .forms import *


class BreedsHome(ListView):
    '''View for main page Cats app'''
    model = Breeds
    template_name = 'cats/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        '''returns some vars to html'''
        context = super().get_context_data(**kwargs)
        # here is where I can add some vars to html, but I moved menu to tags, so I don't need it
        # context['menu'] = menu
        context['cat_selected'] = 0
        context['title'] = 'Cats app. Breeds'
        return context

    def get_queryset(self):
        '''returns data from db to objects'''
        return Breeds.objects.filter(is_published=True)


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


class CreateBreed(CreateView):
    form_class = AddBreedForm
    template_name = 'cats/add.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add a new breed'
        return context


def contact(request):
    return HttpResponse('contact')


def login(request):
    return HttpResponse('login')


class ShowPost(DetailView):
    model = Breeds
    template_name = 'cats/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    # when we use pk instead of slug for URL
    # pk_url_kwarg = 'post_pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.kwargs['post_slug'].title()
        return context


class BreedsCategory(ListView):
    model = Breeds
    template_name = 'cats/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Breeds.objects.filter(category__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['posts'][0].category
        context['cat_selected'] = context['posts'][0].category_id
        return context


def admin_page(request):
    pass
