from django.db import models
from django.contrib.postgres.fields import ArrayField
from polymorphic import models as polymorphic

MODULE_CHOICES = (
    ('abastecimiento', 'Abastecimiento'),
    ('cajero', 'Cajero'),
    ('distribucion', 'Distribucion'),
    ('reservacion', 'Reservacion'),
    ('facturacion', 'Facturacion'),
    ('configuracion', 'Configuracion'),
)


class Institucion(polymorphic.PolymorphicModel):

    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    active_modules = ArrayField(
        models.CharField(max_length=200, choices=MODULE_CHOICES),
        blank=True,
        default=list
    )

    class Meta:
        verbose_name = "Institucion"
        verbose_name_plural = "Instituciones"

    def __str__(self) -> str:
        return self.name
