from django.contrib import admin
from .models import PetaSeabaranModel

# Register your models here.


@admin.register(PetaSeabaranModel)
class PetaSebaranAdmin(admin.ModelAdmin): ...
