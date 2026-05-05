from django.db import models


# Create your models here.
class BaseAssetModel(models.Model):
    CATEGORY_CHOICES = [
        ("danau", "Danau"),
        ("embung", "Embung"),
        ("bendung", "Bendung"),
        ("sedimen", "Sedimen"),
        ("pantai", "Pantai"),
        ("tanggul", "Tanggul"),
        ("sumur", "Sumur"),
        ("absah", "Absah"),
    ]
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=60, choices=CATEGORY_CHOICES)

    # lokasi
    province = models.CharField(max_length=100)
    regency = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    village = models.CharField(max_length=100)

    # latitude = models.FloatField(null=True, blank=True)
    # longitude = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = "tb_asset"
        verbose_name = "Data Asset"
