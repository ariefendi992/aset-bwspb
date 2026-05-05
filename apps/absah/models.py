from django.db import models
from apps.core.models import BaseAssetModel, BaseFotoModel


# Create your models here.
class DataAbsahModel(BaseAssetModel):
    # Data Teknis
    volume = models.FloatField(null=True, blank=True)
    panjang = models.FloatField(null=True, blank=True)
    tinggi = models.FloatField(null=True, blank=True)
    lebar = models.FloatField(null=True, blank=True)

    # Pelaksanaan Konstruksi
    tahun_mulai = models.IntegerField(null=True, blank=True)
    tahun_selesai = models.IntegerField(null=True, blank=True)
    pengelola = models.CharField(max_length=100, default="BWS PB")
    keterangan = models.CharField(max_length=120, null=True, blank=True)
    manfaat = models.CharField(
        max_length=100, null=True, blank=True, default="Air Baku"
    )

    def __str__(self):
        return self.nama

    def get_thumbnail(self):
        return self.dokumentasi.first()

    class Meta:
        db_table = "tb_data_absah"
        verbose_name = "Data Absah"
        verbose_name_plural = "Data Absah"


class FotoDataAbsahModel(BaseFotoModel):
    absah = models.ForeignKey(
        DataAbsahModel, on_delete=models.CASCADE, related_name="dokumentasi"
    )
    image = models.ImageField(upload_to="dokumentasi/absah/", verbose_name="Foto")

    class Meta:
        db_table = "tb_data_absah_dokumentasi"
        verbose_name = "Dokumentasi Data Absah"
        verbose_name_plural = "Dokumentasi Data Absah"
