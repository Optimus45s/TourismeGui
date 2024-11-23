from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

app_name = 'destination'


def destination_index(request):
    return HttpResponse('<h1> Page des destinations ! </h1>')