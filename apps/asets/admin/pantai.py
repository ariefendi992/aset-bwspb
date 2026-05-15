from django.contrib import admin
from apps.asets.models import PengamanPantaiModel
from apps.asets.forms import PengamanPantaiForm


# Register your models here.
class CustomModelAdmin(admin.ModelAdmin):
    exclude = ["created_by"]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(PengamanPantaiModel)
class PengamanPantaiAdmin(CustomModelAdmin):
    form = PengamanPantaiForm
    list_display = [
        "nama",
        "provinsi",
        "kabupaten",
        "kecamatan",
        "desa",
        "kewenangan",
        "jenis_bangunan",
        "panjang",
        "lebar_puncak",
        "kemiringan",
        "material",
        "struktur",
        "tahun_mulai",
        "tahun_selesai",
        "dibangun_oleh",
        "pelindung",
        "lain_lain",
        "lat1",
        "long1",
        "lat2",
        "long2",
    ]

    def lat1(self, obj):
        return obj.latitude

    def long1(self, obj):
        return obj.longitude

    def lat2(self, obj):
        return obj.latitude2

    def long2(self, obj):
        return obj.longitude2

    fieldsets = [
        ("", {"fields": ["nama"]}),
        ("Lokasi", {"fields": ["provinsi", "kabupaten", "kecamatan", "desa"]}),
        (
            "Data Teknis",
            {
                "fields": [
                    "kewenangan",
                    "jenis_bangunan",
                    "panjang",
                    "lebar_puncak",
                    "kemiringan",
                    "material",
                    "struktur",
                ]
            },
        ),
        (
            "Pelaksanaan Konstruksi",
            {"fields": ["tahun_mulai", "tahun_selesai", "dibangun_oleh"]},
        ),
        ("Manfaat", {"fields": ["pelindung", "lain_lain"]}),
        (
            "Koordinat (Decimal Degree)",
            {"fields": ["latitude", "longitude", "latitude2", "longitude2"]},
        ),
    ]
