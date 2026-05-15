from django.db import models
from apps.core.models import BaseAssetModel, BaseFotoModel


# Create your models here.
class BendungModel(BaseAssetModel):
    KONDISI_CHOICE = [
        ("Berfungsi/Baik", "Berfungsi/Baik"),
        ("Berfungsi/Rusak", "Berfungsi/Rusak"),
        ("Rusak Berat", "Rusak Berat"),
    ]

    latitude = None
    longitude = None

    # Data Teknis
    sungai = models.CharField(max_length=100, blank=True, null=True)
    jenis_bendung = models.CharField(max_length=100, blank=True, null=True)
    tinggi = models.FloatField(null=True, blank=True)
    lebar = models.FloatField(null=True, blank=True)
    debit_intake_musim_hujan = models.FloatField(null=True, blank=True)
    debit_intake_musim_kemarau = models.FloatField(null=True, blank=True)

    # Pelaksanaan Konstruksi
    tahun_mulai = models.IntegerField(blank=True, null=True)
    tahun_rehab = models.IntegerField("Tahun Rehab Terakhir", blank=True, null=True)
    kondisi = models.CharField(
        max_length=100, blank=True, null=True, choices=KONDISI_CHOICE
    )

    # Manfaat/Fungsi
    irigasi = models.FloatField(null=True, blank=True)
    lain_lain = models.CharField(max_length=100, null=True, blank=True)

    # Koordinat decimal place
    latitude1 = models.DecimalField(
        null=True, blank=True, max_digits=9, decimal_places=6
    )
    longitude1 = models.DecimalField(
        null=True, blank=True, max_digits=9, decimal_places=6
    )
    latitude2 = models.DecimalField(
        null=True, blank=True, max_digits=9, decimal_places=6
    )
    longitude2 = models.DecimalField(
        null=True, blank=True, max_digits=9, decimal_places=6
    )

    status_aset = models.CharField(max_length=100, null=True, blank=True)
    penamaan_bmn = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.nama

    class Meta:
        db_table = "tb_bendung"
        verbose_name = "Bendung"
        verbose_name_plural = "Bendung"

    def get_thumbnail(self):
        return self.dokumentasi.first()


class FotoBendungModel(BaseFotoModel):
    bendung = models.ForeignKey(
        BendungModel, on_delete=models.CASCADE, related_name="dokumentasi"
    )
    image = models.ImageField(
        upload_to="dokumentasi/bendung/", verbose_name="Foto/Dokumentasi"
    )

    class Meta:
        db_table = "tb_bendung_dokumentasi"
        verbose_name = "Dokumentasi Bendung"
        verbose_name_plural = "Dokumentasi Bendung"
        ordering = ["-created_at"]
