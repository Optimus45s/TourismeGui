from django.urls import path, re_path
from . import views


app_name = 'destination'

urlpatterns = [
    path('', views.destination_index, name='destination_index'),
]