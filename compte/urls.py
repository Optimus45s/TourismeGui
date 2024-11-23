from django.urls import path, re_path
from . import views


app_name = 'compte'


urlpatterns = [
    path('', views.compte_index, name='compte_index'),
]