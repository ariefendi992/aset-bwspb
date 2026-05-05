from django.contrib import admin
from .models import UserModel, PPKModel
from django.contrib.admin import ModelAdmin

# Register your models here.


@admin.register(UserModel)
class UserAdmin(ModelAdmin):
    list_display = ["username", "last_login"]


@admin.register(PPKModel)
class JabatanAdmin(admin.ModelAdmin): ...
