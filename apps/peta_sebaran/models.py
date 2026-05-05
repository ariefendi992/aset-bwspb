from django.db import models
from apps.core.models import *
import os, uuid


# Create your models here.
class PetaSeabaranModel(models.Model):
    def path_file(instance, filename):
        ext = filename.split(".")[-1]
        # nama = f"Danau_{uuid.uuid4()}.{ext}"
        nama = instance.nama.replace(" ", "_")
        return f"peta_sebaran/{nama}.{ext}"

        # return os.path("peta_sebaran/", new_filename)

    nama = models.CharField("Nama File", max_length=100, blank=True)
    jenis = models.CharField("Jenis File", max_length=100, blank=True)

    file = models.FileField("Unggah File", upload_to=path_file, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nama}"

    class Meta:
        db_table = "tb_danau_peta"

    class Meta:
        db_table = "tb_peta_sebaran"
        verbose_name = "Peta Sebaran Aset"
        verbose_name_plural = "Peta Sebaran Aset"
