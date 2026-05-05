from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import ActivityLogModel
from .middleware import get_current_user


@receiver(post_save)
def log_save(sender, instance, created, **kwargs):
    # hindari log untuk activity sendiri
    if sender.__name__ == "ActivityLogModel":
        return

    user = get_current_user()
    if created:
        desc = f"Menambahkan data {sender.__name__}: {getattr(instance, 'nama', '-')}"
    else:
        desc = f"Memperbaharui data {sender.__name__}: {getattr(instance, 'nama', '-')}"

    if user is None or not user.is_authenticated:
        return  # Jika user belum login maka abaikan activity log
    else:
        ActivityLogModel.objects.create(
            user=user,
            action="CREATE" if created else "UPDATE",
            model_name=sender.__name__,
            object_id=instance.pk,
            description=desc,
        )


@receiver(post_delete)
def log_delete(sender, instance, **kwargs):
    if sender.__name__ in ["ActivityLogModel"]:
        return

    user = get_current_user()

    desc = f"Mengahapus data {sender.__name__}: {getattr(instance, 'nama', '-')}"

    if user is None or not user.is_authenticated:
        return  # Jika user belum login maka abaikan activity log
    else:
        ActivityLogModel.objects.create(
            user=user,
            action="DELETE",
            model_name=sender.__name__,
            object_id=instance.pk,
            description=desc,
        )
