from django.contrib import admin
from django.contrib.auth.models import Group
from autenticacion import models
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from comun.admin import register


class UserModelAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Personal info"),
            {"fields": ("first_name", "last_name", "email")},
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
    )
    search_fields = (
        "username",
        "first_name",
        "last_name",
        "email",
    )
    ordering = ("username",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )


def initialize():
    admin.site.unregister(Group)
    register(models)
    admin.register(models.Usuario)(UserModelAdmin)
