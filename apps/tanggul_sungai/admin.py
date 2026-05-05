from django.contrib import admin
from django.utils.html import format_html
from .models import TanggulSungaiModel, FotoTanggulSungaiModel


# Register your models here.
class CustomModelAdmin(admin.ModelAdmin):
    exclude = ["created_by"]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


class FotoTangulSungaiAdmin(admin.TabularInline):
    model = FotoTanggulSungaiModel
    extra = 1


@admin.register(TanggulSungaiModel)
class TanggulSungaiAdmin(CustomModelAdmin):
    inlines = [FotoTangulSungaiAdmin]
    list_display = [
        "nama",
        "kabupaten",
        "panjang_sungai",
        "nama_sungai",
        "das",
        "koordinat_awal",
        "koordinat_akhir",
        "jenis_konstruksi",
        "panjang_tanggul",
        "tinggi_tanggul",
        "kondisi_sisi_kanan",
        "kondisi_sisi_kiri",
        "tahun_pembuatan",
        "status_aset",
        "penamaan_bmn",
        "preview_dok",
    ]

    def koordinat_awal(self, obj):
        return f"{obj.latitude}, {obj.longitude}"

    def koordinat_akhir(self, obj):
        return f"{obj.latitude2}, {obj.longitude2}"

    def preview_dok(seld, obj):
        foto = obj.dokumentasi.order_by("-created_at").first()
        if foto and foto.image:
            return format_html(
                '<img src= "{}" width="80" style="border-radius:5px;" />', foto.image
            )
        return "-"

    fieldsets = [
        ("", {"fields": ["nama"]}),
        ("Lokasi", {"fields": ["kabupaten"]}),
        ("", {"fields": ["panjang_sungai", "nama_sungai", "das"]}),
        ("Koordinat", {"fields": ["koordinat_awal", "koordinat_akhir"]}),
        ("", {"fields": ["jenis_konstruksi", "panjang_tanggul", "tinggi_tanggul"]}),
        ("Kondisi Tanggul", {"fields": ["kondisi_sisi_kanan", "kondisi_sisi_kiri"]}),
        ("", {"fields": ["tahun_pembuatan", "status_aset", "penamaan_bmn"]}),
    ]
