from django.contrib import admin
from .models import ProvinsiModel, KabupatenModel


# Register your models here.
@admin.register(ProvinsiModel)
class ProvinsiAdmin(admin.ModelAdmin): ...


@admin.register(KabupatenModel)
class KabupatenModel(admin.ModelAdmin): ...
