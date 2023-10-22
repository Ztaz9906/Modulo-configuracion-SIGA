from django.db import models
from base.models import TbNestructura
from autenticacion.models.entities.usuario import Usuario
from autenticacion.models.entities.institucion import Institucion
from autenticacion.models.entities.persona import Persona

class TbDelementosMostrar(models.Model):
    id_institucion = models.ForeignKey(Institucion, models.CASCADE)
    id_elementos_mostrar = models.AutoField(primary_key=True)
    elementos_mostrar_menu = models.IntegerField(blank=True, null=True)
    elementos_mostrar_reservacion = models.IntegerField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    elementos_mostrar_calendario = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'tb_delementos_mostrar'

class TbDperiodoReservacion(models.Model):
    id_institucion = models.ForeignKey(Institucion, models.CASCADE)
    id_periodo_reservacion = models.AutoField(primary_key=True)
    periodo_reservacion = models.IntegerField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    class Meta:
        verbose_name='Peridodo de Reservacion'
        db_table = 'tb_dperiodo_reservacion'


class TbDresponsableAreaPersonas(models.Model):
    id_institucion = models.ForeignKey(Institucion, models.CASCADE)
    id_responsable_area_personas = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey(
        Persona, models.DO_NOTHING, db_column='id_persona', blank=True, null=True, related_name='id_persona_resp_area')
    id_estructura = models.ForeignKey(
        TbNestructura, models.DO_NOTHING, db_column='id_estructura', blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    id_persona_registro = models.ForeignKey(
        Usuario, models.DO_NOTHING, db_column='id_persona_registro', blank=True, null=True)

    class Meta:

        db_table = 'tb_dresponsable_area_personas'


class TbDresponsableReservacion(models.Model):
    id_responsable_reservacion = models.AutoField(primary_key=True)
    id_institucion = models.ForeignKey(Institucion, models.CASCADE)
    id_persona = models.ForeignKey(
        Persona, models.DO_NOTHING, db_column='id_persona', blank=True, null=True, related_name='id_persona_responsable')
    id_estructura = models.ForeignKey(
        TbNestructura, models.DO_NOTHING, db_column='id_estructura', blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    id_persona_registro = models.ForeignKey(
        Usuario, models.DO_NOTHING, db_column='id_persona_registro', blank=True, null=True)

    class Meta:

        db_table = 'tb_dresponsable_reservacion'

