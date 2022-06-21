from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse, request


from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from register.forms import PlayListForm


# Create your views here.

@login_required(login_url='/login')
def home(response):
    searched = response.POST.get('searched', "")
    song = Song.objects.filter(Title__contains=searched)
    user = Account.objects.all()
    return render(response, "main/home.html", {"song": song, "acc": user})


@login_required(login_url='/login')
def base(response):
    song = Song.objects.all()
    return render(response, "main/index.html", {"song": song})


@login_required(login_url='/login') #https://www.youtube.com/watch?v=EX6Tt-ZW0so&ab_channel=DennisIvy
def profile(response):
    form = PlayListForm()
    user = response.user
    if response.method == 'POST':
        form = PlayListForm(response.POST)
        form.instance.idUser = user
        if form.is_valid():
            form.save()

    return render(response, "main/profile.html", {"PlayListForm": form})

