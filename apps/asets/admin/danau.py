from django.contrib import admin
from apps.asets.models import DanauModel


# Register your models here.
class CustomModelAdmin(admin.ModelAdmin):
    exclude = ["created_by"]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(DanauModel)
class DanauAdmin(CustomModelAdmin):
    list_display = [
        "nama",
        "lat",
        "lon",
        "desa",
        "kecamatan",
        "tp_danau",
        "l_genangan",
        "_volume",
        "_irigasi",
        "ternak",
        "air_baku",
        "plta",
        "_volume_tampungan",
        "permasalahan",
        "keterangan",
    ]
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
                    # "latitude",
                    # "longitude",
                ]
            },
        ),
        (
            "Koordinat",
            {
                "fields": ["latitude", "longitude"],
            },
        ),
        (
            "Data teknis",
            {
                "fields": [
                    "tipe_danau",
                    "luas_genangan",
                    "volume",
                ]
            },
        ),
        (
            "Fungsi",
            {
                "fields": [
                    "irigasi",
                    "ternak",
                    "air_baku",
                    "plta",
                ]
            },
        ),
        (
            "",
            {"fields": ["volume_tampungan", "permasalahan", "keterangan"]},
        ),
    ]
    # fieldsets = [("Data teknis", {"fields": ["tipe_danau", "luas_genangan"]})]

    def lat(self, obj):
        return obj.latitude

    def lon(self, obj):
        return obj.longitude

    def tp_danau(self, obj):
        return obj.tipe_danau

    def l_genangan(self, obj):
        return obj.luas_genangan

    def _volume(self, obj):
        if obj.volume is None:
            return "-"

        # tambah jt di belakang angka
        return f"{obj.volume} jt"

    def _irigasi(self, obj):
        if obj.irigasi is None:
            return "-"

        return (
            f"{obj.irigasi:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        )

    def _volume_tampungan(self, obj):
        if obj.volume_tampungan is None:
            return "-"

        # tambah jt di belakang angka
        return f"{obj.volume_tampungan} jt"
