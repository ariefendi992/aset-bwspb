from django.db import models
from uuid import uuid4
from django.conf import settings
from django.contrib.auth import get_user_model
import os

User = get_user_model()


# Create your models here.
class BaseAssetModel(models.Model):
    PROVINSI_CHOICE = [
        ("Papua Barat", "Papua Barat"),
        ("Papua Barat Daya", "Papua Barat Daya"),
    ]

    KABUPATEN_CHOICE = [
        ("Kabupaten Manokwari", "Kabupaten Manokwari"),
        ("Kabupaten Manokwari Selatan", "Kabupaten Manokwari Selatan"),
        ("Kabupaten Maybrat", "Kabupaten Maybrat"),
        ("Kabupaten Pegunungan Arfak", "Kabupaten Pegunungan Arfak"),
        ("Kabupaten Teluk Bintuni", "Kabupaten Teluk Bintuni"),
        ("Kabupaten Teluk Wondama", "Kabupaten Teluk Wondama"),
        ("kabupaten Kaimana", "Kabupaten Kaimana"),
        ("kabupaten Fakfak", "Kabupaten Fakfak"),
        ("Kota Sorong", "Kota Sorong"),
        ("Kabupaten Sorong", "Kabupaten Sorong"),
        ("kabupaten Raja Ampat", "Kabupaten Raja Ampat"),
    ]

    nama = models.CharField(max_length=255)
    provinsi = models.CharField(
        max_length=100, choices=PROVINSI_CHOICE, null=True, blank=True
    )
    # provinsi = models.CharField(max_length=100, null=True, blank=True)
    kabupaten = models.CharField(
        max_length=100,
        verbose_name="Kabupaten/Kota",
        choices=KABUPATEN_CHOICE,
        null=True,
        blank=True,
    )
    kecamatan = models.CharField(max_length=100, null=True, blank=True)
    desa = models.CharField("Desa/Kelurahan", max_length=100, null=True, blank=True)

    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_created",  # ✅ FIX
    )

    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_updated",  # ✅ FIX
    )

    class Meta:
        abstract = True
        # db_table = "tb_asset"
        # verbose_name = "Asset Data"


class BasePetaSebaranModel(models.Model):
    def upload_to(instance, filename):
        ext = filename.split(".")[-1]

        new_filename = f"{uuid4().hex}_{instance.nama_file}.{ext}"

        return os.path.join("peta_sebaran/", new_filename)

    ASET_CHOICE = [
        ("Danau", "Danau"),
        ("Embung", "Embung"),
        ("Bendung", "Bendung"),
        ("Sedimen", "Sedimen"),
        ("Pantai", "Pantai"),
        ("Tanggul", "Tanggul"),
        ("Sumur", "Sumur"),
        ("Absah", "Absah"),
    ]

    nama_file = models.CharField(max_length=100, null=True, blank=True)
    jenis_aset = models.CharField(
        max_length=100, choices=ASET_CHOICE, verbose_name="Jenis Aset"
    )
    file_peta = models.FileField(
        upload_to=upload_to, null=True, blank=True, verbose_name="Pilih File"
    )

    class Meta:
        abstract = True


class BaseFotoModel(models.Model):

    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ActivityLogModel(models.Model):
    ACTION_CHOICES = [
        ("CREATE", "CREATE"),
        ("UPDATE", "UPDATE"),
        ("DELETE", "DELETE"),
    ]
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    action = models.CharField(max_length=16, choices=ACTION_CHOICES)
    model_name = models.CharField(max_length=100)
    # data_name = models.CharField(max_length=120)
    object_id = models.IntegerField()
    description = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.action} - {self.model_name}"

    class Meta:
        db_table = "tb_activity"
