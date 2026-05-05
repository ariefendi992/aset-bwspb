from django.db import models
from apps.core.models import BaseAssetModel, BaseFotoModel


# Create your models here.
class CheckDamModel(BaseAssetModel):
    # Data Teknis
    volume_sabo = models.FloatField(
        null=True, blank=True, verbose_name="Volume Sabo (m3)"
    )
    panjang = models.FloatField(null=True, blank=True, verbose_name="Panjang (m)")
    tinggi = models.FloatField(null=True, blank=True, verbose_name="Tinggi (m)")
    lebar = models.FloatField(null=True, blank=True, verbose_name="Lebar (m)")

    # Pelaksanaan Konstruksi
    tahun_mulai = models.IntegerField("Tahun Mulai", null=True, blank=True)
    tahun_selesai = models.IntegerField("Tahun Selesai", null=True, blank=True)
    pengelola = models.CharField(max_length=100, null=True, blank=True)
    keterangan = models.CharField("Keterangan", max_length=120, null=True, blank=True)

    # Manfaat/Fungsi
    irigasi = models.FloatField("Irigasi (Ha)", null=True, blank=True)
    lain = models.CharField("Lain-lain", max_length=100, null=True, blank=True)

    # Koordinat (Decimal Degree)
    latitude2 = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    longitude2 = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )

    status_aset = models.CharField("Status Aset", max_length=100, null=True, blank=True)
    penamaan_bmn = models.CharField(
        max_length=120, blank=True, null=True, verbose_name="Penamaan BMN"
    )

    def __str__(self):
        return self.nama

    def get_thumbnail(self):
        return self.dokumentasi.first()

    class Meta:
        db_table = "tb_checkdam"
        verbose_name = "Pengendali Sedimen"
        verbose_name_plural = "Pengendali Sedimen"


class FotoCheckDamModel(BaseFotoModel):
    checkdam = models.ForeignKey(
        CheckDamModel, on_delete=models.CASCADE, related_name="dokumentasi"
    )
    image = models.ImageField(upload_to="dokumentasi/checkdam/", verbose_name="foto")

    class Meta:
        db_table = "tb_checkdam_dokumentasi"
