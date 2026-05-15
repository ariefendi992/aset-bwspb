from django.db import models
from apps.core.models import BaseAssetModel, BasePetaSebaranModel
import os, uuid


# Create your models here.
class DanauModel(BaseAssetModel):

    # Data Teknis
    tipe_danau = models.CharField(max_length=100, null=True, blank=True)
    luas_genangan = models.FloatField(
        null=True, blank=True, verbose_name="Luas Genangan (Ha)"
    )
    volume = models.FloatField(null=True, blank=True, verbose_name="Volume (m3)")

    # Fungsi
    irigasi = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Irigasi (Ha)",
    )
    ternak = models.IntegerField(null=True, blank=True, verbose_name="Ternak (ekor)")
    air_baku = models.FloatField(
        null=True, blank=True, verbose_name="Air Baku (ltr/dtk)"
    )
    plta = models.FloatField(null=True, blank=True, verbose_name="PLTA (KWh)")

    volume_tampungan = models.FloatField(
        null=True, blank=True, verbose_name="Volume Tampungan Saat Ini (m3)"
    )
    permasalahan = models.TextField(
        null=True, blank=True, verbose_name="Permasalahan di Danau"
    )
    keterangan = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nama

    class Meta:
        db_table = "tb_danau"
        verbose_name = "Danau"
        verbose_name_plural = "Danau"
        unique_together = ["nama"]


# class PetaDanauModel(models.Model):

#     def path_file(instance, filename):
#         ext = filename.split(".")[-1]
#         new_filename = f"Danau_{uuid.uuid4()}.{ext}"
#         return os.path("peta_sebaran/", new_filename)


#     nama = models.CharField("Nama File", max_length=100)
#     files = models.FileField("Unggah File", upload_to=path_file)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.nama}"

#     class Meta:
#         db_table = "tb_danau_peta"
