from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

app_name = 'compte'

def compte_index(request):
    return HttpResponse('<h1> Page utilisateur ! </h1>')