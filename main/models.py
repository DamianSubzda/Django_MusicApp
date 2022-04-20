from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    premiumStatus = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Song(models.Model):
    IdSong = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=101)
    Time = models.CharField(max_length=20)
    Performer = models.CharField(max_length=100)
    CreationDate = models.DateTimeField()
    Mp3 = models.FileField(blank=True, null=True)

    def __str__(self):
        return str(self.IdSong) + self.Title


class Singer(models.Model):
    IdSinger = models.AutoField(primary_key=True)
    fName = models.CharField(max_length=100)
    sName = models.CharField(max_length=100)
    Pseudonym = models.CharField(max_length=100)

    def __str__(self):
        return str(self.IdSinger) + self.fName + self.sName


class FavouriteSong(models.Model):
    IdSong = models.ForeignKey(Song, on_delete=models.CASCADE)
    IdUser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Song_Singer(models.Model):
    IdSong = models.ForeignKey(Song, on_delete=models.CASCADE)
    IdSinger = models.ForeignKey(Singer, on_delete=models.CASCADE)
