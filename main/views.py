from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(response):
    return render(response, "main/home.html", {})

def profile(response):
    return render(response, "main/profile.html", {})

def test(response):
    return HttpResponse("Hello world!")