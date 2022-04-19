from django.shortcuts import render
from django.http import HttpResponse, request
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(response):
    return render(response, "main/home.html", {})


def base(response):
    return render(response, "main/index.html", {})


@login_required(login_url='/login')
def profile(response):
    return render(response, "main/profile.html", {})


def test(response):
    return HttpResponse("Hello world!")


def payU(response):
    return HttpResponse("Succes!")
