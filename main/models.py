from django.db import models


# Create your models here.
# python manage.py makemigrations css
# python manage.py migrate

class Member(models.Model): #TODO
    IdUser = models.AutoField(primary_key=True)
    Nick = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    fName = models.CharField(max_length=100)
    sName = models.CharField(max_length=100)
    PremiumStatus = models.BooleanField(default=False)
    JoinDate = models.DateTimeField(auto_now_add=True) #default=datatime

    def __str__(self):
        return str(self.Nick)

class Song(models.Model):
    IdSong = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=101)
    Time = models.IntegerField()
    Performer = models.CharField(max_length=100)
    CreationDate = models.DateTimeField()
    Mp3 = models.FileField() #FileFiled

    def __str__(self):
        return str(self.IdSong + self.Title)

class Singer(models.Model):
    IdSinger = models.AutoField(primary_key=True)
    fName = models.CharField(max_length=100)
    sName = models.CharField(max_length=100)
    Pseudonym = models.CharField(max_length=100)

    def __str__(self):
        return str(self.IdSinger + self.fName + self.sName)

class FavouriteSong(models.Model): #TODO
    IdUser = models.ForeignKey(Member, on_delete=models.CASCADE)
    IdSong = models.ForeignKey(Song, on_delete=models.CASCADE)

class Song_Singer(models.Model):
    IdSong = models.ForeignKey(Song, on_delete=models.CASCADE)
    IdSinger = models.ForeignKey(Singer, on_delete=models.CASCADE)
