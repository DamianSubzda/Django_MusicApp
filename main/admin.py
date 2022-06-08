from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *


class CustomUserAdmin(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'Accounts'

class CustomizedUserAdmin(UserAdmin):
    inlines = (CustomUserAdmin, )

admin.site.unregister(User)

admin.site.register(User, CustomizedUserAdmin)
admin.site.register(Singer)
admin.site.register(PlayList)
admin.site.register(Song)