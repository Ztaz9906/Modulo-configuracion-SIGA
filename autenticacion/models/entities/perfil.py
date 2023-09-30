from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import signals
from django.dispatch import receiver
from django.contrib import admin
from polymorphic import models as polymorphic

from autenticacion.models.entities.usuario import Usuario


class Perfil(polymorphic.PolymorphicModel):
    """Representa un perfil."""

    user = models.OneToOneField(
        Usuario, on_delete=models.CASCADE, related_name="perfil", verbose_name="usuario"
    )

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"

    class Admin(admin.ModelAdmin):
        list_display = ["id", "user"]


# noinspection PyUnusedLocal
@receiver(signals.post_delete, sender=Perfil)
def on_delete_profile(sender, instance: Perfil, **kwargs):
    try:
        instance.user.delete()
    except ObjectDoesNotExist:
        ...
