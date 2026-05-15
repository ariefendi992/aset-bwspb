from django.contrib import admin
from apps.asets.models import BendungModel, FotoBendungModel
from django.utils.html import format_html


# Register your models here.
class CustomModelAdmin(admin.ModelAdmin):
    exclude = ["created_by"]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


class FotoBendungAdmin(admin.TabularInline):
    model = FotoBendungModel
    extra = 1


@admin.register(BendungModel)
class BendungAdmin(CustomModelAdmin):
    list_display = [
        "nama",
        "provinsi",
        "kabupaten",
        "kecamatan",
        "desa",
        "sungai",
        "jenis_bendung",
        "tinggi",
        "lebar",
        "debit_intake_musim_hujan",
        "debit_intake_musim_kemarau",
        "tahun_mulai",
        "tahun_rehab",
        "kondisi",
        "irigasi",
        "lain_lain",
        "latitude1",
        "longitude1",
        "latitude2",
        "longitude2",
        "status_aset",
        "penamaan_bmn",
        "preview_dok",
    ]

    def preview_dok(seld, obj):
        foto = obj.dokumentasi.order_by("-created_at").first()
        if foto and foto.image:
            return format_html(
                '<img src= "{}" width="80" style="border-radius:5px;" />', foto.image
            )
        return "-"

    fieldsets = [
        ("", {"fields": ["nama"]}),
        ("Lokasi", {"fields": ["provinsi", "kabupaten", "kecamatan", "desa"]}),
        (
            "Koordinat (Decimal Degree)",
            {"fields": ["latitude1", "longitude1", "latitude2", "longitude2"]},
        ),
        (
            "Data Teknis",
            {
                "fields": [
                    "tinggi",
                    "lebar",
                    "debit_intake_musim_hujan",
                    "debit_intake_musim_kemarau",
                ]
            },
        ),
        (
            "Pelaksanaan Konstruksi",
            {"fields": ["tahun_mulai", "tahun_rehab", "kondisi"]},
        ),
        ("Manfaat", {"fields": ["irigasi", "lain_lain"]}),
        ("", {"fields": ["status_aset", "penamaan_bmn"]}),
    ]

    inlines = [FotoBendungAdmin]
