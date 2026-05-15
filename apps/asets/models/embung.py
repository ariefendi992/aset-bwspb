from django.db import models
from apps.core.models import BaseAssetModel


# Create your models here.
class EmbungModel(BaseAssetModel):
    # Data Teknis
    provinsi = None
    tipe_konstruksi = models.CharField(max_length=100, null=True, blank=True)
    luas_genangan = models.FloatField(null=True, blank=True)
    volume_tampungan = models.FloatField(blank=True, null=True)
    lebar = models.FloatField(blank=True, null=True)
    panjang = models.FloatField(blank=True, null=True)
    tinggi = models.FloatField(blank=True, null=True)

    # Fungsi
    irigasi = models.DecimalField(
        null=True,
        blank=True,
        max_digits=12,
        decimal_places=2,
        verbose_name="Irigasi (Ha)",
    )
    ternak = models.IntegerField(null=True, blank=True, verbose_name="Ternak (ekor)")
    air_baku = models.FloatField(
        null=True, blank=True, verbose_name="Air Baku (ltr/dtk)"
    )
    lainnya = models.CharField(max_length=100, null=True, blank=True)

    # Kondisi Infrakstruktur
    kondisi = models.CharField(
        max_length=100,
        choices=[
            ("Baik", "Baik"),
            ("Rusak Ringan", "Rusak Ringan"),
            ("Rusak Berat", "Rusak Berat"),
        ],
    )

    volume_saat = models.FloatField(
        null=True, blank=True, verbose_name="Volume Saat Ini (m3)"
    )
    keterangan = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nama

    class Meta:
        db_table = "tb_embung"
        verbose_name = "Embung"
        verbose_name_plural = "Embung"
