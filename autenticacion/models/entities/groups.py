from django.contrib.auth.models import Group as OriginalGroup
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import GroupAdmin


class Group(OriginalGroup):
    """Representa un grupo."""

    class Meta:
        proxy = True
        verbose_name = _("Grupo")
        verbose_name_plural = _("Grupos")

    class Admin(GroupAdmin):
        ...
