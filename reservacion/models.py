from django.db import models
from base.models import TbDpersona, TbNestructura
from adminschema.models import TbUser


class TbDelementosMostrar(models.Model):
    id_elementos_mostrar = models.AutoField(primary_key=True)
    elementos_mostrar_menu = models.IntegerField(blank=True, null=True)
    elementos_mostrar_reservacion = models.IntegerField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    elementos_mostrar_calendario = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'tb_delementos_mostrar'


class TbDperiodoReservacion(models.Model):
    id_periodo_reservacion = models.AutoField(primary_key=True)
    periodo_reservacion = models.IntegerField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)

    class Meta:

        db_table = 'tb_dperiodo_reservacion'


class TbDresponsableAreaPersonas(models.Model):
    id_responsable_area_personas = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey(
        TbDpersona, models.DO_NOTHING, db_column='id_persona', blank=True, null=True, related_name='id_persona_resp_area')
    id_estructura = models.ForeignKey(
        TbNestructura, models.DO_NOTHING, db_column='id_estructura', blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    id_persona_registro = models.ForeignKey(
        TbUser, models.DO_NOTHING, db_column='id_persona_registro', blank=True, null=True)

    class Meta:

        db_table = 'tb_dresponsable_area_personas'


class TbDresponsableReservacion(models.Model):
    id_responsable_reservacion = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey(
        TbDpersona, models.DO_NOTHING, db_column='id_persona', blank=True, null=True, related_name='id_persona_responsable')
    id_estructura = models.ForeignKey(
        TbNestructura, models.DO_NOTHING, db_column='id_estructura', blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    id_persona_registro = models.ForeignKey(
        TbUser, models.DO_NOTHING, db_column='id_persona_registro', blank=True, null=True)

    class Meta:

        db_table = 'tb_dresponsable_reservacion'

# por que esta tabla no tiene relacion con ninguna en la base de datos revisar


class TbHistorialReservacion(models.Model):
    id_historial_reservacion = models.AutoField(primary_key=True)
    id_persona = models.CharField(max_length=1)
    usuario_platos = models.JSONField(blank=True, null=True)
    costo = models.FloatField(blank=True, null=True)
    fecha_reservacion = models.DateField(blank=True, null=True)
    fecha_cancelacion = models.DateField(blank=True, null=True)
    por_plato = models.BooleanField(blank=True, null=True)
    id_configuracion_cobro = models.IntegerField(blank=True, null=True)
    id_menu = models.IntegerField()
    activo = models.BooleanField(blank=True, null=True)
    cobrada = models.BooleanField(blank=True, null=True)
    id_evento = models.IntegerField()
    id_reservacion = models.IntegerField()

    class Meta:

        db_table = 'tb_historial_reservacion'
