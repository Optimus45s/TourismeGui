from django.urls import path, re_path
from . import views

app_name = 'blog'


urlpatterns = [
    path('', views.blog_index, name='blog_index'),
]