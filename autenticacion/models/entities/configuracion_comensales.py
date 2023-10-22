from django.db import models
from autenticacion.models.entities.institucion import Institucion


class TbDconfiguracionPersona(models.Model):
    id_configuracion_persona = models.AutoField(primary_key=True)
    id_institucion = models.ForeignKey(Institucion, models.CASCADE)
    activo = models.BooleanField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name='Configuracion Personas'
        db_table = 'tb_dconfiguracion_persona'