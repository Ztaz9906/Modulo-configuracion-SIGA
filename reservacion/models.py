from django.db import models
from cajero.models import TbNevento, TbDpersonaDistribucion, TbDmenu, TbNplato
from configuracion.models import TbDconfiguracionCobro
from base.models import TbDpersona , TbNestructura
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

class TbDreservacion(models.Model):
    id_reservacion = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey(TbDpersona, models.DO_NOTHING, db_column='id_persona', blank=True, null=True)
    id_evento = models.ForeignKey(TbNevento, models.DO_NOTHING, db_column='id_evento', blank=True, null=True)
    fecha_reservacion = models.DateField(blank=True, null=True)
    activo = models.BooleanField()
    fecha_cancelacion = models.DateField(blank=True, null=True)
    costo_reservacion = models.FloatField(blank=True, null=True)
    es_por_plato = models.BooleanField(blank=True, null=True)
    id_menu = models.IntegerField(blank=True, null=True) # verificar por que este campo no hace referencia a ningun otro en la base de datos 
    token_reservacion = models.TextField(blank=True, null=True)
    cobrada = models.BooleanField(blank=True, null=True)
    id_configuracion_cobro = models.ForeignKey(TbDconfiguracionCobro, models.DO_NOTHING, db_column='id_configuracion_cobro', blank=True, null=True)
    id_persona_distribucion = models.ForeignKey(TbDpersonaDistribucion, models.DO_NOTHING, db_column='id_persona_distribucion', blank=True, null=True)
    guardado = models.BooleanField(blank=True, null=True)

    class Meta:
        
        db_table = 'tb_dreservacion'

class TbDresponsableAreaPersonas(models.Model):
    id_responsable_area_personas = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey(TbDpersona, models.DO_NOTHING, db_column='id_persona', blank=True, null=True)
    id_estructura = models.ForeignKey(TbNestructura, models.DO_NOTHING, db_column='id_estructura', blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    id_persona_registro = models.ForeignKey(TbUser, models.DO_NOTHING, db_column='id_persona_registro', blank=True, null=True)
    class Meta:
        
        db_table = 'tb_dresponsable_area_personas'

class TbDresponsableReservacion(models.Model):
    id_responsable_reservacion = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey(TbDpersona, models.DO_NOTHING, db_column='id_persona', blank=True, null=True)
    id_estructura = models.ForeignKey(TbNestructura, models.DO_NOTHING, db_column='id_estructura', blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    id_persona_registro = models.ForeignKey(TbUser, models.DO_NOTHING, db_column='id_persona_registro', blank=True, null=True)

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

class TbRreservacionPlato(models.Model):
    id_reservacion_plato = models.AutoField(primary_key=True)
    id_reservacion = models.ForeignKey(TbDreservacion, models.DO_NOTHING, db_column='id_reservacion', blank=True, null=True)
    id_plato = models.ForeignKey(TbNplato, models.DO_NOTHING, db_column='id_plato', blank=True, null=True)
    id_menu = models.ForeignKey(TbDmenu, models.DO_NOTHING, db_column='id_menu', blank=True, null=True)
    id_evento = models.ForeignKey(TbNevento, models.DO_NOTHING, db_column='id_evento', blank=True, null=True)
    id_persona = models.ForeignKey(TbDpersona, models.DO_NOTHING, db_column='id_persona', blank=True, null=True)
    guardado = models.BooleanField(blank=True, null=True)

    class Meta:
        
        db_table = 'tb_rreservacion_plato'

class TbRticketReservacion(models.Model):
    id_ticket_reservacion = models.AutoField(primary_key=True)
    ticket = models.TextField(blank=True, null=True)
    id_reservacion = models.ForeignKey(TbDreservacion, models.DO_NOTHING, db_column='id_reservacion', blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    id_usuario_registro = models.ForeignKey(TbUser, models.DO_NOTHING, db_column='id_persona_registro', blank=True, null=True)

    class Meta:
        
        db_table = 'tb_rticket_reservacion'