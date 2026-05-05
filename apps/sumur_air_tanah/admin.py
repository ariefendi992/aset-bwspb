from django.contrib import admin
from .models import SumurAirTanahModel


# Register your models here.
class CustomModelAdmin(admin.ModelAdmin):
    exclude = ["created_by"]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(SumurAirTanahModel)
class SumurAirTanahAdmin(CustomModelAdmin):
    list_display = [
        "nama",
        "jenis_sumur",
        "kedalaman_sumur",
        "jenis_pompa",
        "debit_pompa",
        "tahun_pembangunan",
        "das",
        "ws",
        "latitude",
        "longitude",
        "kecamatan",
        "kabupaten",
        "keterangan",
    ]

    fieldsets = [
        (
            "",
            {
                "fields": [
                    "nama",
                    "jenis_sumur",
                    "kedalaman_sumur",
                    "jenis_pompa",
                    "debit_pompa",
                    "tahun_pembangunan",
                    "das",
                    "ws",
                ]
            },
        ),
        (
            "Lokasi",
            {
                "fields": [
                    "latitude",
                    "longitude",
                    "kecamatan",
                    "kabupaten",
                ]
            },
        ),
        ("", {"fields": ["keterangan"]}),
    ]
