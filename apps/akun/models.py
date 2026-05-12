from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser

# Create your models here.
# class UserManager(BaseUserManager):

#     def create_user(self, nama_depan, nama_belakang, email, password):
#         user = self.model(
#             email=self.normalize_email(email),
#             nama_depan=nama_depan,
#             nama_belakang=nama_belakang,
#         )
#         user.set_password(password)
#         user.save(using=self.db)
#         return user

#     def create_superuser(self, nama_depan, nama_belakang, email, password):
#         user = self.create_user(
#             nama_depan=nama_depan,
#             nama_belakang=nama_belakang,
#             email=email,
#             password=password,
#         )

#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self.db)
#         return user


# class User(AbstractBaseUser):
#     role = [
#         ("satker", "Satker"),
#         ("ppk", "PPK"),
#         ("staff", "staff"),
#     ]
#     nama_depan = models.CharField(max_length=40)
#     nama_belakang = models.CharField(max_length=60)
#     email = models.EmailField(max_length=100, unique=True)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)

#     objects = UserManager()

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ["nama_depan", "nama_belakang"]

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         return True

#     def has_modeule_perms(self, app_label):
#         return True


class PPKModel(models.Model):
    nama = models.CharField(max_length=100, blank=True)
    kode = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.nama

    class Meta:
        db_table = "tb_ppk"
        verbose_name = "PPK"
        verbose_name_plural = "PPK"


class SatkerModel(models.Model):
    nama = models.CharField(max_length=100, blank=True)
    kode = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.nama

    class Meta:
        db_table = "tb_satker"
        verbose_name = "Satker"
        verbose_name_plural = "Satker"


class UserModel(AbstractUser):
    role = [
        ("", "-- Pilih --"),
        ("ppk", "PPK"),
        ("staff_ppk", "Staff PPK"),
        ("staff_satker", "Staff Satker"),
    ]

    role = models.CharField(
        "Role", max_length=30, choices=role, blank=True, null=True, default=""
    )
    ppk = models.ForeignKey(
        PPKModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    satker = models.ForeignKey(
        SatkerModel, on_delete=models.SET_NULL, null=True, blank=True
    )
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username}"

    @property
    def nama(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = "tb_user"
        verbose_name = "Pengguna"
        verbose_name_plural = "Data Pengguna"
