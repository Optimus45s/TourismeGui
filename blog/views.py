from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


app_name = 'blog'


def blog_index(request):
    return HttpResponse("<h1>Voici le Blog !</h1>")