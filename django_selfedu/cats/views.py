from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView, TemplateView

from .models import *
from .forms import *
from .utils import *


class BreedsHome(DataMixin, ListView):
    '''View for main page Cats app'''
    model = Breeds
    template_name = 'cats/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        '''returns some vars to html'''
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Cats app. Breeds')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        '''returns data from db to objects'''
        return Breeds.objects.filter(is_published=True).select_related('category')


class CreateBreed(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddBreedForm
    template_name = 'cats/add.html'
    success_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Add a new breed')
        return dict(list(context.items()) + list(c_def.items()))


class ShowPost(DataMixin, DetailView):
    model = Breeds
    template_name = 'cats/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    # when we use pk instead of slug for URL
    # pk_url_kwarg = 'post_pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class BreedsCategory(DataMixin, ListView):
    model = Breeds
    template_name = 'cats/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Breeds.objects.filter(category__slug=self.kwargs['cat_slug'], is_published=True).select_related(
            'category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        title = context['posts'][0].category
        c_def = self.get_user_context(title=title,
                                      cat_selected=title.id)
        return dict(list(context.items()) + list(c_def.items()))


# Views for users
class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'cats/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Authentication')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'cats/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Sign Up")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


def logout_user(request):
    logout(request)
    return redirect('login')


# Some helpful page
class AboutPage(DataMixin, TemplateView):
    template_name = 'cats/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='About site')
        return dict(list(context.items()) + list(c_def.items()))


def admin_page(request):
    return reverse_lazy('admin')


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'cats/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Feedback')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


def page_not_found(request, exception):
    return HttpResponseNotFound(
        f'<h1>requested page is not found, please enter correct address or visit another page</h1>'
        '<a href="{% url "home" %}">home</a>'
        f'<p>cat</p>')
