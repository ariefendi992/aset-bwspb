from django.contrib import admin
from apps.asets.models import EmbungModel


# Register your models here.
class CustomModelAdmin(admin.ModelAdmin):
    exclude = ["created_by"]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(EmbungModel)
class EmbungAdmin(CustomModelAdmin):
    list_display = [
        "nama",
        "lat",
        "lon",
        "desa",
        "kecamatan",
        "kabupaten",
        "tipe_konstruksi",
        "volume_tampungan",
        "lebar",
        "panjang",
        "tinggi",
        "irigasi",
        "ternak",
        "lainnya",
        "kondisi",
        "volume_saat",
    ]

    def lat(self, obj):
        return obj.latitude

    def lon(self, obj):
        return obj.longitude

    fieldsets = [
        ("", {"fields": ["nama"]}),
        (
            "Lokasi",
            {"fields": ["latitude", "longitude", "desa", "kecamatan", "kabupaten"]},
        ),
        (
            "Data Teknis",
            {
                "fields": [
                    "tipe_konstruksi",
                    "luas_genangan",
                    "volume_tampungan",
                    "lebar",
                    "panjang",
                    "tinggi",
                ]
            },
        ),
        ("Fungsi", {"fields": ["irigasi", "ternak", "air_baku", "lainnya"]}),
        ("Kondisi Infrastruktur", {"fields": ["kondisi"]}),
        ("", {"fields": ["volume_saat", "keterangan"]}),
    ]
