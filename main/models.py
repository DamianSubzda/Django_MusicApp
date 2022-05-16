from datetime import datetime

import mutagen
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth.models import User

from mutagen.mp3 import MP3

from main.helpers import get_audio_length


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    premiumStatus = models.BooleanField(default=False)
    #timeSpendListening = models.DecimalField(max_length=20, blank=True, max_digits=20, decimal_places=2)

    def __str__(self):
        return self.user.username

    def addTime(self, time):
        self.timeSpendListening += time


class Song(models.Model):
    IdSong = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=101)
    Time = models.DecimalField(max_length=20, blank=True, max_digits=20, decimal_places=2)
    Performer = models.CharField(max_length=100)
    AddingDate = models.DateTimeField()
    Mp3 = models.FileField(blank=True, null=True)

    def __str__(self):
        return str(self.IdSong) + " " + self.Title

    def save(self, *args, **kwargs):
        if not self.Time:
            audio_length = get_audio_length(self.Mp3)
            self.Time = audio_length
        return super().save(*args, **kwargs)

    def getDuration(self):
        seconds = self.Time
        hours = seconds // (60 * 60)
        seconds %= (60 * 60)
        minutes = seconds // 60
        seconds %= 60
        if hours != 0:
            return "%02i:%02i:%02i" % (hours, minutes, seconds)
        return "%02i:%02i" % (minutes, seconds)


class Singer(models.Model):
    IdSinger = models.AutoField(primary_key=True)
    fName = models.CharField(max_length=100)
    sName = models.CharField(max_length=100)
    Pseudonym = models.CharField(max_length=100)

    def __str__(self):
        return str(self.IdSinger) + " " + self.fName + " " + self.sName


class FavouriteSong(models.Model):
    IdSong = models.ForeignKey(Song, on_delete=models.CASCADE)
    IdUser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Song_Singer(models.Model):
    IdSong = models.ForeignKey(Song, on_delete=models.CASCADE)
    IdSinger = models.ForeignKey(Singer, on_delete=models.CASCADE)
