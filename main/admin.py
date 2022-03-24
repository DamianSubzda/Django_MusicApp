from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(Member)
admin.site.register(Song)
admin.site.register(Singer)
admin.site.register(Song_Singer)
admin.site.register(FavouriteSong)