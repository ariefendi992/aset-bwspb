from django.db import models
from apps.core.models import BaseAssetModel


# Create your models here.
class SumurAirTanahModel(BaseAssetModel):
    provinsi = None
    latitude = models.DecimalField(
        null=True, blank=True, max_digits=10, decimal_places=7
    )
    longitude = models.DecimalField(
        null=True, blank=True, max_digits=10, decimal_places=7
    )
    jenis_sumur = models.CharField(max_length=50, null=True, blank=True)
    kedalaman_sumur = models.FloatField(null=True, blank=True)
    jenis_pompa = models.CharField(max_length=100, null=True, blank=True)
    debit_pompa = models.FloatField("Debit Pompa (l/dtk)", null=True, blank=True)
    tahun_pembangunan = models.IntegerField(null=True, blank=True)
    das = models.CharField("DAS", max_length=100, null=True, blank=True)
    ws = models.CharField("WS", max_length=100, null=True, blank=True)
    keterangan = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.nama

    class Meta:
        db_table = "tb_sumur_air_tanah"
        verbose_name = "Sumur Air Tanah"
        verbose_name_plural = "Sumur Air Tanah"
