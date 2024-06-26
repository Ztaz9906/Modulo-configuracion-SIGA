from django.contrib.auth import models as auth
from django.db import models
from django.utils.translation import gettext_lazy as _
from autenticacion.models.entities.institucion import Institucion
from autenticacion.models.entities.persona import Persona


class Usuario(auth.AbstractUser):
    """Representa un usuario."""
    email = models.EmailField(_("email address"), unique=True)
    institucion = models.ForeignKey(
        Institucion, on_delete=models.CASCADE, null=True, blank=True)
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE, blank=True,null=True)

    class Meta(auth.AbstractUser.Meta):
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
