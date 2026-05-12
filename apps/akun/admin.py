from django.contrib import admin
from .models import UserModel, PPKModel, SatkerModel
from django.contrib.auth.admin import UserAdmin

# Register your models here.


@admin.register(UserModel)
class UserAdmin(UserAdmin):
    list_display = ["username", "nama", "last_login", "role", "ppk", "satker"]

    # fieldsets = [
    #     (
    #         "",
    #         {
    #             "classes": ["wide"],
    #             "fields": [
    #                 "username",
    #                 "password",
    #             ],
    #         },
    #     )
    # ]

    fieldsets = (
        (
            None,
            {"fields": ("username", "password", "role")},
        ),
        ("Data Personal", {"fields": ["first_name", "last_name", "ppk", "satker"]}),
        (
            "Permissions",
            {
                # "classes": ["wide", "collapse"],
                "fields": [
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    # "user_permissions",
                ],
            },
        ),
        (
            "Important Dates",
            {"classes": ["wide"], "fields": ["last_login", "date_joined"]},
        ),
    )
    add_fieldsets = (
        (
            None,
            {"fields": ("username", "password1", "password2", "is_active", "role")},
        ),
        ("Data Personal", {"fields": ["first_name", "last_name", "ppk", "satker"]}),
    )


# @admin.register(PPKModel)
# class JabatanAdmin(admin.ModelAdmin): ...


# @admin.register(SatkerModel)
# class SatkerAdmin(admin.ModelAdmin): ...
