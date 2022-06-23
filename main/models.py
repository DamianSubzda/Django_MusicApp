from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth.models import User
from main.helpers import get_audio_length


class Singer(models.Model):
    idSinger = models.AutoField(primary_key=True, null=False, blank=False)
    fName = models.CharField(max_length=100, null=False, blank=False)
    sName = models.CharField(max_length=100, null=False, blank=False)
    pseudonym = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return str(self.idSinger) + " " + self.fName + " " + self.sName


class Team(models.Model):
    Name = models.CharField(primary_key=True, max_length=100, null=False, blank=False)
    singers = models.ManyToManyField(Singer)

    def __str__(self):
        return self.Name


class Song(models.Model):
    IdSong = models.AutoField(primary_key=True, null=False, blank=False)
    Title = models.CharField(max_length=101, null=False, blank=False)
    Time = models.DecimalField(max_length=20, blank=True, max_digits=20, decimal_places=2)
    Team = models.ForeignKey("Team", on_delete=models.CASCADE, null=False, blank=False)
    AddingDate = models.DateTimeField(null=False, blank=False)
    Mp3 = models.FileField(upload_to='music', null=False, blank=False)
    Image = models.ImageField(upload_to='image', null=True, blank=True)

    def __str__(self):
        return self.Title

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


class PlayList(models.Model):
    idUser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=False)
    title = models.CharField(max_length=101, null=False, blank=False)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.title
