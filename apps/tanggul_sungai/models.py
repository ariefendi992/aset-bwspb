from django.db import models
from apps.core.models import BaseAssetModel, BaseFotoModel


# Create your models here.
class TanggulSungaiModel(BaseAssetModel):
    provinsi = None
    kecamatan = None
    desa = None
    # latitude = None
    # longitude = None

    lokasi_sungai = models.CharField(max_length=100, null=True, blank=True)
    panjang_sungai = models.FloatField(null=True, blank=True)
    nama_sungai = models.CharField(max_length=120, null=True, blank=True)
    das = models.CharField(max_length=100, null=True, blank=True)
    latitude2 = models.DecimalField(
        null=True, blank=True, max_digits=9, decimal_places=6
    )
    longitude2 = models.DecimalField(
        null=True, blank=True, max_digits=9, decimal_places=6
    )
    jenis_konstruksi = models.CharField(
        max_length=120,
        null=True,
        blank=True,
        choices=[
            ("Talud Pasang Batu", "Talud Pasang Batu"),
            ("Pasang Batu", "Pasang Batu"),
            ("Bronjong", "Bronjong"),
        ],
    )
    panjang_tanggul = models.FloatField(null=True, blank=True)
    tinggi_tanggul = models.FloatField(null=True, blank=True)
    kondisi_sisi_kanan = models.CharField(max_length=100, null=True, blank=True)
    kondisi_sisi_kiri = models.CharField(max_length=100, null=True, blank=True)
    tahun_pembuatan = models.IntegerField(null=True, blank=True)
    status_aset = models.CharField(max_length=100, null=True, blank=True)
    penamaan_bmn = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.nama

    def get_thumbnail(self):
        return self.dokumentasi.first()

    class Meta:
        db_table = "tb_tanggul_sungai"
        verbose_name = "Tanggul Sungai"
        verbose_name_plural = "Tanggul Sungai"


class FotoTanggulSungaiModel(BaseFotoModel):
    tanggul = models.ForeignKey(
        TanggulSungaiModel, on_delete=models.CASCADE, related_name="dokumentasi"
    )
    image = models.ImageField("File Dokumentasi", upload_to="dokumentasi/tanggul/")

    class Meta:
        db_table = "tb_tanggul_sungai_dokumentasi"
        verbose_name = "Dokumentasi Tanggul Sungai"
        verbose_name_plural = "Dokumentasi Tanggul Sungai"
