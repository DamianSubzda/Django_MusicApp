from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("<h1>Hello world!</h1>")

def index2(response):
    return HttpResponse("<h1>Bye world!</h1>")