from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *

admin.site.register(Singer)
admin.site.register(PlayList)
admin.site.register(Friend)
admin.site.register(Song)
admin.site.register(Team)