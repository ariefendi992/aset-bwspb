from django.contrib import admin
from apps.asets.models import DataAbsahModel, FotoDataAbsahModel
from django.utils.html import format_html


# Register your models here.
class CustomModelAdmin(admin.ModelAdmin):
    exclude = ["created_by"]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


class DokumentasiDataAbsahAdmin(admin.TabularInline):
    model = FotoDataAbsahModel
    extra = 1


@admin.register(DataAbsahModel)
class DataAbsahAdmin(CustomModelAdmin):

    list_display = [
        "nama",
        "provinsi",
        "kabupaten",
        "kecamatan",
        "desa",
        "latitude",
        "longitude",
        "volume",
        "panjang",
        "tinggi",
        "lebar",
        "tahun_mulai",
        "tahun_selesai",
        "pengelola",
        "keterangan",
        "preview_dok",
    ]

    def preview_dok(seld, obj):
        foto = obj.dokumentasi.order_by("-created_at").first()
        if foto and foto.image:
            return format_html(
                '<img src= "{}" width="80" style="border-radius:5px;" />', foto.image
            )
        return "-"

    inlines = [DokumentasiDataAbsahAdmin]

    fieldsets = [
        ("", {"fields": ["nama"]}),
        (
            "Lokasi",
            {
                "fields": [
                    "provinsi",
                    "kabupaten",
                    "kecamatan",
                    "desa",
                ]
            },
        ),
        ("Koordinat", {"fields": ["latitude", "longitude"]}),
        ("Data Teknis", {"fields": ["panjang", "tinggi", "lebar"]}),
        (
            "Pelaksanaan Konstruksi",
            {"fields": ["tahun_mulai", "tahun_selesai", "pengelola"]},
        ),
        ("", {"fields": ["manfaat"]}),
    ]
