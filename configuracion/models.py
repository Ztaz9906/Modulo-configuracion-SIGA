from django.db import models
from adminschema.models import TbUser
from cajero.models import TbStructure,TbNevento, TbNdiaSemana
from base.models import TbNcategoria,TbNcategoriaResidente,TbNestructura, TbNtipoCurso

class TbDavisos(models.Model):
    id_aviso = models.AutoField(primary_key=True)
    titulo = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    id_usuario_registro = models.IntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'tb_davisos'


class TbDconfiguracionCobro(models.Model):
    id_configuracion_cobro = models.AutoField(primary_key=True)
    activo = models.BooleanField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)

    class Meta:
        
        db_table = 'tb_dconfiguracion_cobro'


#### no se ahce
class TbDconfiguracionElastic(models.Model):
    id_configuracion_elastic = models.AutoField(primary_key=True)
    ip = models.TextField(blank=True, null=True)
    puerto = models.TextField(blank=True, null=True)
    config_indice = models.TextField(blank=True, null=True)
    fecha_registro = models.DateTimeField(blank=True, null=True)
    id_usuario_registro = models.ForeignKey(TbUser, models.DO_NOTHING, db_column='id_usuario_registro')

    class Meta:
        
        db_table = 'tb_dconfiguracion_elastic'

##### se puede quitar por que esta muy estricto y crea conflictos 
class TbDconfiguracionEventoAcceso(models.Model):
    id_configuracion_evento_acceso = models.AutoField(primary_key=True)
    activo = models.BooleanField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)

    class Meta:
        
        db_table = 'tb_dconfiguracion_evento_acceso'

###Aqui manda config comensales
class TbDconfiguracionPersona(models.Model):
    id_configuracion_persona = models.AutoField(primary_key=True)
    activo = models.BooleanField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)

    class Meta:
        
        db_table = 'tb_dconfiguracion_persona'

### se ponen 3 campos incambiable 3 datos estaticos se activa o se desactiva 
class TbDconfiguracionProceso(models.Model):
    id_configuracion_proceso = models.AutoField(primary_key=True)
    flujo = models.BooleanField(blank=True, null=True)
    descripcion_configuracion_proceso = models.TextField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    id_usuario_registro = models.ForeignKey(TbUser, models.DO_NOTHING, db_column='id_usuario_registro')

    class Meta:
        
        db_table = 'tb_dconfiguracion_proceso'

#### no se ahce
class TbDconfiguracionRabbitmq(models.Model):
    id_configuracion_rabbitmq = models.AutoField(primary_key=True)
    ip = models.TextField(blank=True, null=True)
    puerto = models.TextField(blank=True, null=True)
    fecha_registro = models.DateTimeField(blank=True, null=True)
    id_usuario_registro = models.ForeignKey(TbUser, models.DO_NOTHING, db_column='id_usuario_registro')
    usuario = models.TextField(blank=True, null=True)
    contrasena = models.TextField(blank=True, null=True)

    class Meta:
        
        db_table = 'tb_dconfiguracion_rabbitmq'


#### no se ahce tareas programadas
class TbDcron(models.Model):
    id_cron = models.AutoField(primary_key=True)
    scrip = models.TextField(blank=True, null=True)
    frecuencia = models.IntegerField(blank=True, null=True)
    ultima_actualizacion = models.DateTimeField(blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)
    unidad_tiempo = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    id_usuario_registro = models.ForeignKey(TbUser, models.DO_NOTHING, db_column='id_usuario_registro')
    proxima_actualizacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        
        db_table = 'tb_dcron'


class TbDdatosContacto(models.Model):
    id_datos_contacto = models.AutoField(primary_key=True)
    direccion = models.TextField(blank=True, null=True)
    telefono = models.TextField(blank=True, null=True)
    correo = models.TextField(blank=True, null=True)
    id_usuario_registro = models.ForeignKey(TbUser, models.DO_NOTHING, db_column='id_usuario_registro')
    fecha_registro = models.DateField(blank=True, null=True)

    class Meta:
        
        db_table = 'tb_ddatos_contacto'


class TbDplanificacionMenu(models.Model):
    id_planificacion_menu = models.AutoField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    cantidad_reservaciones_desayuno = models.IntegerField(blank=True, null=True)
    cantidad_por_configuracion_desayuno = models.IntegerField(blank=True, null=True)
    planificacion_desayuno = models.IntegerField(blank=True, null=True)
    cantidad_reservaciones_almuerzo = models.IntegerField(blank=True, null=True)
    cantidad_por_configuracion_almuerzo = models.IntegerField(blank=True, null=True)
    planificacion_almuerzo = models.IntegerField(blank=True, null=True)
    cantidad_reservaciones_comida = models.IntegerField(blank=True, null=True)
    cantidad_por_configuracion_comida = models.IntegerField(blank=True, null=True)
    planificacion_comida = models.IntegerField(blank=True, null=True)
    id_complejo = models.ForeignKey(TbStructure, models.DO_NOTHING, db_column='id_complejo')

    class Meta:
        
        db_table = 'tb_dplanificacion_menu'


class TbDvaloresConfiguracionCobro(models.Model):
    id_valores_configuracion_cobro = models.AutoField(primary_key=True)
    id_configuracion_cobro = models.ForeignKey(TbDconfiguracionCobro, models.DO_NOTHING, db_column='id_configuracion_cobro', blank=True, null=True)
    id_categoria = models.ForeignKey(TbNcategoria, models.DO_NOTHING, db_column='id_categoria', blank=True, null=True)
    id_categoria_residente = models.ForeignKey(TbNcategoriaResidente, models.DO_NOTHING, db_column='id_categoria_residente', blank=True, null=True)
    id_estructura = models.ForeignKey(TbNestructura, models.DO_NOTHING, db_column='id_estructura', blank=True, null=True)
    id_tipo_curso = models.ForeignKey(TbNtipoCurso, models.DO_NOTHING, db_column='id_tipo_curso', blank=True, null=True)
    id_tipo_cobro = models.IntegerField(blank=True, null=True) # hay q hacer la relacion con el esquema de cobro en la tabla tipo de cobro  
    precio = models.FloatField(blank=True, null=True)
    id_evento = models.ForeignKey(TbNevento, models.DO_NOTHING, db_column='id_evento', blank=True, null=True)

    class Meta:
        
        db_table = 'tb_dvalores_configuracion_cobro'


class TbDvaloresConfiguracionEventoAcceso(models.Model):
    id_valores_configuracion_evento_acceso = models.AutoField(primary_key=True)
    id_categoria = models.ForeignKey(TbNcategoria, models.DO_NOTHING, db_column='id_categoria', blank=True, null=True)
    id_estructura = models.ForeignKey(TbNestructura, models.DO_NOTHING, db_column='id_estructura', blank=True, null=True)
    id_tipo_curso = models.ForeignKey(TbNtipoCurso, models.DO_NOTHING, db_column='id_tipo_curso', blank=True, null=True)
    id_evento = models.ForeignKey(TbNevento, models.DO_NOTHING, db_column='id_evento', blank=True, null=True)
    id_categoria_residente = models.ForeignKey(TbNcategoriaResidente, models.DO_NOTHING, db_column='id_categoria_residente', blank=True, null=True)
    id_configuracion_evento_acceso = models.ForeignKey(TbDconfiguracionEventoAcceso, models.DO_NOTHING, db_column='id_configuracion_evento_acceso')
    id_dia_semana = models.ForeignKey(TbNdiaSemana, models.DO_NOTHING, db_column='id_dia_semana', blank=True, null=True)

    class Meta:
        
        db_table = 'tb_dvalores_configuracion_evento_acceso'


class TbDvaloresConfiguracionPersona(models.Model):
    id_calores_configuracion_persona = models.AutoField(primary_key=True)
    id_configuracion_persona = models.ForeignKey(TbDconfiguracionPersona, models.DO_NOTHING, db_column='id_configuracion_persona', blank=True, null=True)
    id_categoria = models.ForeignKey(TbNcategoria, models.DO_NOTHING, db_column='id_categoria', blank=True, null=True)
    id_categoria_residente = models.ForeignKey(TbNcategoriaResidente, models.DO_NOTHING, db_column='id_categoria_residente', blank=True, null=True)
    id_estructura = models.ForeignKey(TbNestructura, models.DO_NOTHING, db_column='id_estructura', blank=True, null=True)
    id_tipo_curso = models.ForeignKey(TbNtipoCurso, models.DO_NOTHING, db_column='id_tipo_curso', blank=True, null=True)

    class Meta:
        
        db_table = 'tb_dvalores_configuracion_persona'
