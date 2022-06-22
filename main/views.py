from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from main.forms import PlayListForm
from django import template

from .templatetags.has_group import has_group


@login_required(login_url='/login')
def home(response):
    searched = response.POST.get('searched', "")
    song = Song.objects.filter(Title__contains=searched)
    user = User.objects.all()
    playList = PlayList.objects.filter(idUser=response.user)
    return render(response, "main/home.html", {"song": song, "acc": user, "playList": playList})


@login_required(login_url='/login')
def search_playlist(response, playlist):
    instance = PlayList.objects.filter(id=playlist)
    song = instance[0].songs.all()
    user = User.objects.all()
    return render(response, "main/home.html", {"song": song, "acc": user})


@login_required(login_url='/login')
def base(response):
    song = Song.objects.all()
    return render(response, "main/index.html", {"song": song})


@login_required(login_url='/login')
def profile(response):
    form = PlayListForm()
    user = response.user

    if response.method == 'POST':
        form = PlayListForm(response.POST)
        form.instance.idUser = user

        if response.user.is_superuser:
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/profile")
        else:
            if not has_group(user, "premiumUser"):
                if len(PlayList.objects.filter(idUser=response.user)) < 2:
                    if form.is_valid():
                        form.save()
                        return HttpResponseRedirect("/profile")
            else:
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect("/profile")
    playList = PlayList.objects.filter(idUser=response.user)
    return render(response, "main/profile.html", {"PlayListForm": form, "playList": playList})


@login_required(login_url='/login')
def delete_playlist(request, id):
    instance = PlayList.objects.filter(id=id)
    instance.delete()
    return HttpResponseRedirect("/profile")


@login_required(login_url='/login')
def delete_song(request, id, song):
    instance = PlayList.objects.filter(id=id)
    instance[0].songs.remove(song)
    return HttpResponseRedirect("/profile")


@login_required(login_url='/login')  # Sprawdzić czy dana piosenka jest już w Playliście!
def add_song(request, playlist_id, song_id):
    playlists = PlayList.objects.filter(id=playlist_id)
    songs = Song.objects.filter(IdSong=song_id)
    print(playlists)
    print(songs)
    playlists[0].songs.add(songs[0])
    playlists[0].save()
    return HttpResponseRedirect("/home")
