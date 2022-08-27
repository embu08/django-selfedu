from django.urls import include, path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', BreedsHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('add/', CreateBreed.as_view(), name='add'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('post/<slug:post_slug>', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>', BreedsCategory.as_view(), name='category'),
    path('admin/', admin_page, name='admin'),
]
