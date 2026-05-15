from django.contrib import admin
from apps.asets.models import CheckDamModel, FotoCheckDamModel
from django.utils.html import format_html
from apps.asets.forms import CheckDamForm


# Register your models here.
class CustomModelAdmin(admin.ModelAdmin):
    exclude = ["created_by"]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


class DokumentasiCheckDamAdmin(admin.TabularInline):
    model = FotoCheckDamModel
    extra = 1


@admin.register(CheckDamModel)
class CheckDamAdmin(CustomModelAdmin):
    form = CheckDamForm
    list_display = [
        "nama",
        "provinsi",
        "kabupaten",
        "kecamatan",
        "desa",
        "volume_sabo",
        "panjang",
        "tinggi",
        "lebar",
        "tahun_mulai",
        "tahun_selesai",
        "pengelola",
        "keterangan",
        "irigasi",
        "lain",
        "lat1",
        "long1",
        "lat2",
        "long2",
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

    inlines = [DokumentasiCheckDamAdmin]

    fieldsets = [
        ("", {"fields": ["nama"]}),
        ("Lokasi", {"fields": ["provinsi", "kabupaten", "kecamatan", "desa"]}),
        ("Data Teknis", {"fields": ["volume_sabo", "panjang", "tinggi", "lebar"]}),
        (
            "Pelaksanaan Konstruksi",
            {"fields": ["tahun_mulai", "tahun_selesai", "pengelola", "keterangan"]},
        ),
        ("Manfaat", {"fields": ["irigasi", "lain"]}),
        (
            "Koordinat (Decimal Degree)",
            {"fields": ["latitude", "longitude", "latitude2", "longitude2"]},
        ),
        ("", {"fields": ["status_aset", "penamaan_bmn"]}),
    ]

    def lat1(self, obj):
        return obj.latitude

    def long1(self, obj):
        return obj.longitude

    def lat2(self, obj):
        return obj.latitude2

    def long2(self, obj):
        return obj.longitude2
