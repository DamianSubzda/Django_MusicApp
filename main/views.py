from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse, request
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(response):
    song = Song.objects.all()
    return render(response, "main/home.html", {"song": song})


def base(response):
    song = Song.objects.all()
    return render(response, "main/index.html", {"song": song})


@login_required(login_url='/login')
def profile(response):
    song = Song.objects.all()
    return render(response, "main/profile.html", {"song": song})

