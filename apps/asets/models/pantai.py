from django.db import models
from apps.core.models import BaseAssetModel, BaseFotoModel


# Create your models here.
class PengamanPantaiModel(BaseAssetModel):
    # Data teknis
    JENIS_BANGUNAN_CHOICE = [
        ("Revetman", "Revetman"),
        ("Break Water", "Break Water"),
        ("Seawall", "Seawall"),
        ("Pasangan Batu", "Pasangan Batu"),
        ("Tanggul Laut", "Tanggul Laut"),
        # ("Revetman", "Revetman"),
        # ("Revetman", "Revetman"),
    ]
    kewenangan = models.CharField(max_length=100, null=True, blank=True)
    jenis_bangunan = models.CharField(max_length=100, choices=JENIS_BANGUNAN_CHOICE)
    panjang = models.FloatField(null=True, blank=True)
    lebar_puncak = models.FloatField(null=True, blank=True)
    kemiringan = models.CharField(max_length=100, null=True, blank=True)
    material = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        choices=[
            ("Beton", "Beton"),
            ("Pasangan Batu", "Pasangan Batu"),
        ],
    )
    struktur = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        choices=[
            ("Buis Beton", "Buis Beton"),
            ("Kubus Beton", "Kubus Beton"),
            ("Talud", "Talud"),
        ],
    )

    # Pelaksanaan Konstruksi
    tahun_mulai = models.IntegerField(blank=True, null=True)
    tahun_selesai = models.IntegerField(blank=True, null=True)
    dibangun_oleh = models.CharField(max_length=100, default="BWS PB")

    # Manfaat
    pelindung = models.CharField(max_length=100, null=True, blank=True)
    lain_lain = models.CharField(max_length=100, null=True, blank=True)

    # Koordinat (Decimal Degree)
    latitude2 = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    longitude2 = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )

    def __str__(self):
        return self.nama

    class Meta:
        db_table = "tb_pengaman_pantai"
        verbose_name = "Pengaman Pantai"
        verbose_name_plural = "Pengaman Pantai"
