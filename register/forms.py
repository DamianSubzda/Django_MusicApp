from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from main.models import PlayList

class RegisterForm(UserCreationForm):

    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["email", "username", "password1", "password2"]


class PlayListForm(ModelForm):
    class Meta:
        model = PlayList
        fields = ['title']
