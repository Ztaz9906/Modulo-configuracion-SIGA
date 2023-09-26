from django.db import models
from base.models import TbDpersona
from adminschema.models import TbUser, TbInstitucion
from django.contrib.postgres.fields import ArrayField
######################################################################## Pertenece a distibucion ################################


class TbCategory(models.Model):
    id_institucion = models.ForeignKey(TbInstitucion, models.CASCADE)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    color = models.TextField()

    class Meta:
        db_table = 'tb_category'

    def __str__(self):
        """Return String"""
        return self.name


class TbNclasificacionEvento(models.Model):
    id_institucion = models.ForeignKey(TbInstitucion, models.CASCADE)
    id_clasificacion_evento = models.AutoField(primary_key=True)
    nombre_clasificacion_evento = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    descripcion_clasificacion_evento = models.TextField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'tb_nclasificacion_evento'

class TbNdiaSemana(models.Model):
    id_dia_semana = models.AutoField(primary_key=True)
    dia_semana = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return self.dia_semana

    class Meta:
        db_table = 'tb_ndia_semana'

class TbNhorario(models.Model):
   
    id_institucion = models.ForeignKey(TbInstitucion, models.CASCADE)
    id_horario = models.AutoField(primary_key=True)
    dias_semana = models.ManyToManyField(TbNdiaSemana)
    nombre_horario = models.TextField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    activo = models.BooleanField()

    class Meta:
        db_table = 'tb_nhorario'


class TbNevento(models.Model):
    id_institucion = models.ForeignKey(TbInstitucion, models.CASCADE)
    id_evento = models.AutoField(primary_key=True)
    nombre_evento = models.TextField(blank=True, null=True)
    activo = models.BooleanField()
    descripcion_evento = models.TextField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    id_clasificacion_evento = models.ForeignKey(
        TbNclasificacionEvento, models.DO_NOTHING, db_column='id_clasificacion_evento', blank=True, null=True)
    accesos = models.IntegerField(blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)
    evento_padre = models.ForeignKey(
        'self', models.DO_NOTHING, db_column='evento_padre', blank=True, null=True)
    id_horario = models.ForeignKey(
        TbNhorario, models.DO_NOTHING, db_column='id_horario', blank=True, null=True)
    icono = models.TextField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.nombre_evento
    class Meta:
        db_table = 'tb_nevento'


class TbStructure(models.Model):
    id_institucion = models.ForeignKey(TbInstitucion, models.CASCADE)
    category = models.ForeignKey(TbCategory, models.DO_NOTHING)
    estructura_parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    name = models.TextField()
    initials = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    version = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    capacidad = models.IntegerField(blank=True, null=True)
    id_sub_director = models.ForeignKey(TbDpersona, models.DO_NOTHING, db_column='id_sub_director',
                                        blank=True, null=True, related_name='id_sub_director_Structure')
    id_tecnico_general = models.ForeignKey(TbDpersona, models.DO_NOTHING, db_column='id_tecnico_general',
                                           blank=True, null=True, related_name='id_tecnico_general_Structure')
    centro_costo = models.TextField(blank=True, null=True)
    id_especialista_complejo = models.ForeignKey(
        TbDpersona, models.DO_NOTHING, db_column='id_especialista_complejo', blank=True, null=True, related_name='id_especialista_complejo_Structure')

    class Meta:
        db_table = 'tb_structure'

    def __str__(self):
        """Return String"""
        return self.name
######################################################################## Final ############################################

######################################################################## Abastecimiento con asset ###################################################


class TbNclasificacionPlato(models.Model):
    id_institucion = models.ForeignKey(TbInstitucion, models.CASCADE)
    id_clasificacion_plato = models.AutoField(primary_key=True)
    nombre_clasificacion_plato = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    descripcion_clasificacion_plato = models.TextField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'tb_nclasificacion_plato'


class TbNtipoProducto(models.Model):
    id_institucion = models.ForeignKey(TbInstitucion, models.CASCADE)
    id_tipo_producto = models.AutoField(primary_key=True)
    nombre_tipo_producto = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    descripcion_tipo_producto = models.TextField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'tb_ntipo_producto'


class TbNunidadMedida(models.Model):
    id_institucion = models.ForeignKey(TbInstitucion, models.CASCADE)
    id_unidad_medida = models.AutoField(primary_key=True)
    nombre_unidad_medida = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    descripcion_unidad_medida = models.TextField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    siglas = models.TextField(blank=True, null=True)
    clasificacion = models.TextField(blank=False, null=False)

    class Meta:
        db_table = 'tb_nunidad_medida'

####### Empieza esquema asset ##########


class TbDproducto(models.Model):
    id_institucion = models.ForeignKey(TbInstitucion, models.CASCADE)
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    precio_cup = models.FloatField(blank=True, null=True)
    id_tipo_producto = models.ForeignKey(
        TbNtipoProducto, models.DO_NOTHING, db_column='id_tipo_producto')
    id_unidad_medida = models.ForeignKey(TbNunidadMedida, models.DO_NOTHING, db_column='id_unidad_medida',
                                         blank=True, null=True, related_name='id_unidad_medida_producto')  # revisar abastecimiento tambien

    class Meta:
        db_table = 'tb_dproducto'

######### Termina esquema assets #########


class TbDconfiguracionProducto(models.Model):
    id_configuracion_producto = models.AutoField(primary_key=True)
    gramaje = models.FloatField(blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    activo = models.BooleanField()
    fecha_registro = models.DateField(blank=True, null=True)
    id_usuario_registro = models.ForeignKey(
        TbUser, models.DO_NOTHING, db_column='id_usuario_registro', blank=True, null=True)
    id_producto = models.ForeignKey(TbDproducto, models.DO_NOTHING, db_column='id_producto',
                                    blank=True, null=True, related_name='id_producto_config')
    valor_merma = models.FloatField(blank=True, null=True)
    cantidad_disponible = models.FloatField(blank=True, null=True)
    fecha_actualizacion = models.DateField(blank=True, null=True)
    entidad_actualiza = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'tb_dconfiguracion_producto'

# Configuraciones de cantidad de accesos para eventos secundarios ej:doble tiene valor por defecto tiene q existir y solo se puede modificar, para diferentes instituciones hay que ahcer un crud


class TbDaccesoEventoSecundario(models.Model):
    id_institucion = models.ForeignKey(TbInstitucion, models.CASCADE)
    id_acceso_evento_secundario = models.AutoField(primary_key=True)
    cantidad_acceso = models.IntegerField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'tb_dacceso_evento_secundario'


class TbDpersonaIPPuerta(models.Model):
    id_institucion = models.ForeignKey(TbInstitucion, models.CASCADE)
    id_persona_puerta = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey(
        TbDpersona, models.DO_NOTHING, db_column='id_persona', blank=True, null=True)  # quitar ya no hace falta
    id_puerta = models.ForeignKey(
        TbStructure, models.DO_NOTHING, db_column='id_puerta', blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    id_usuario_registro = models.ForeignKey(TbUser, models.DO_NOTHING, db_column='id_usuario_registro',
                                            blank=True, null=True, related_name='id_usuario_registro_personaPuerta')
    fecha_registro = models.DateField(blank=True, null=True)
    id_usuario_modificacion = models.ForeignKey(TbUser, models.DO_NOTHING, db_column='id_usuario_modificacion',
                                                blank=True, null=True, related_name='id_usuario_modificacion_personaPuerta')
    fecha_modificacion = models.DateField(blank=True, null=True)
    # revisar por que hay 2 id puerta en esta tabla
    ip_puerta = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'tb_dpersona_puerta'


class TbDsolapinPerdido(models.Model):
    id_institucion = models.ForeignKey(TbInstitucion, models.CASCADE)
    id_solapin_perdido = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey(
        TbDpersona, models.DO_NOTHING, db_column='id_persona', blank=True, null=True, related_name='id_persona_solapin_perdido')
    codigo_solapin = models.CharField(max_length=1, blank=True, null=True)
    fecha_registro = models.DateTimeField(blank=True, null=True)
    id_usuario_registro = models.ForeignKey(
        TbUser, models.DO_NOTHING, db_column='id_usuario_registro', blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)

    class Meta:
        db_table = 'tb_dsolapin_perdido'


class TbNestadoTarjeta(models.Model):
    id_institucion = models.ForeignKey(TbInstitucion, models.CASCADE)
    id_estado_tarjeta = models.AutoField(primary_key=True)
    nombre_estado_tarjeta = models.CharField(max_length=255)
    fecha_registro = models.DateField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)

    class Meta:
        db_table = 'tb_nestado_tarjeta'


class TbNtipoTarjeta(models.Model):
    id_institucion = models.ForeignKey(TbInstitucion, models.CASCADE)
    id_tipo_tarjeta = models.AutoField(primary_key=True)
    nombre_tipo_tarjeta = models.CharField(max_length=255)
    fecha_registro = models.DateField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'tb_ntipo_tarjeta'


class TbDtarjetaAlimentacion(models.Model):
    id_institucion = models.ForeignKey(TbInstitucion, models.CASCADE)
    id_tarjeta_alimentacion = models.AutoField(primary_key=True)
    codigo = models.TextField(blank=True, null=True, default='12345COD')
    numero_serie = models.TextField(blank=True, null=True, default='12345NO')
    id_estado_tarjeta = models.ForeignKey(
        TbNestadoTarjeta, models.DO_NOTHING, db_column='id_estado_tarjeta', blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    id_usuario_registro = models.ForeignKey(TbUser, models.DO_NOTHING, db_column='id_usuario_registro',
                                            blank=True, null=True, related_name='id_usuario_registro_tarjetaAlimentacion')
    id_tipo_tarjeta = models.ForeignKey(
        TbNtipoTarjeta, models.DO_NOTHING, db_column='id_tipo_tarjeta', blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    id_usuario_modificacion = models.ForeignKey(TbUser, models.DO_NOTHING, db_column='id_usuario_modificacion',
                                                blank=True, null=True, related_name='id_usuario_modificacion_tarjetaAlimentacion')

    class Meta:
        db_table = 'tb_dtarjeta_alimentacion'

################################################################ Distribucion #################################################################


class TbNclasificacionDistribucion(models.Model):
    id_institucion = models.ForeignKey(TbInstitucion, models.CASCADE)
    id_clasificacion_distribucion = models.AutoField(primary_key=True)
    nombre = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'tb_nclasificacion_distribucion'


class TbDdistribucion(models.Model):
    id_institucion = models.ForeignKey(TbInstitucion, models.CASCADE)
    id_distribucion = models.AutoField(primary_key=True)
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    id_usuario_registro = models.ForeignKey(
        TbUser, models.DO_NOTHING, db_column='id_usuario_registro', blank=True, null=True)
    id_clasificacion_distribucion = models.ForeignKey(
        TbNclasificacionDistribucion, models.DO_NOTHING, db_column='id_clasificacion_distribucion', blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    fecha_distribucion = models.DateField(blank=True, null=True)
    id_evento = models.ForeignKey(
        TbNevento, models.DO_NOTHING, db_column='id_evento', blank=True, null=True)
    activo = models.BooleanField()
    es_principal = models.BooleanField(blank=True, null=True)

    class Meta:
        db_table = 'tb_ddistribucion'


class TbDpersonaDistribucion(models.Model):
    id_institucion = models.ForeignKey(TbInstitucion, models.CASCADE)
    id_persona_distribucion = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey(
        TbDpersona, models.DO_NOTHING, db_column='id_persona', blank=True, null=True, related_name='id_persona_dist')
    id_usuario_registro = models.ForeignKey(
        TbUser, models.DO_NOTHING, db_column='id_usuario_registro', blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    id_usuario_modificacion = models.ForeignKey(TbUser, models.DO_NOTHING, db_column='id_usuario_modificacion',
                                                blank=True, null=True, related_name='id_usuario_modificacion_distribucionpersona')
    id_distribucion = models.ForeignKey(TbDdistribucion, models.DO_NOTHING, db_column='id_distribucion',
                                        blank=True, null=True, related_name='id_distribucion_persona')
    id_complejo_comedor = models.ForeignKey(TbStructure, models.DO_NOTHING, db_column='id_complejo_comedor',
                                            blank=True, null=True, related_name='id_complejo_comedor_distribucionpersona')
    id_comedor = models.ForeignKey(TbStructure, models.DO_NOTHING, db_column='id_comedor',
                                   blank=True, null=True, related_name='id_comedor_persona')
    id_puerta = models.ForeignKey(TbStructure, models.DO_NOTHING, db_column='id_puerta',
                                  blank=True, null=True, related_name='id_puerta_persona')
    id_evento = models.ForeignKey(TbNevento, models.DO_NOTHING, db_column='id_evento',
                                  blank=True, null=True, related_name='id_evento_persona')

    class Meta:
        db_table = 'tb_dpersona_distribucion'


class TbDtarjetaDistribucion(models.Model):
    id_institucion = models.ForeignKey(TbInstitucion, models.CASCADE)
    id_tarjeta_distribucion = models.AutoField(primary_key=True)
    id_usuario_registro = models.ForeignKey(
        TbUser, models.DO_NOTHING, db_column='id_usuario_registro', blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    id_usuario_modificacion = models.ForeignKey(TbUser, models.DO_NOTHING, db_column='id_usuario_modificacion',
                                                blank=True, null=True, related_name='id_usuario_modificacion_distribucion')
    id_distribucion = models.ForeignKey(TbDdistribucion, models.DO_NOTHING, db_column='id_distribucion',
                                        blank=True, null=True, related_name='id_distribucion_tarjeta')
    id_complejo_comedor = models.ForeignKey(TbStructure, models.DO_NOTHING, db_column='id_complejo_comedor',
                                            blank=True, null=True, related_name='id_complejo_comedor_tarjeta')
    id_comedor = models.ForeignKey(TbStructure, models.DO_NOTHING, db_column='id_comedor',
                                   blank=True, null=True, related_name='id_comedor_tarjeta')
    id_puerta = models.ForeignKey(TbStructure, models.DO_NOTHING, db_column='id_puerta',
                                  blank=True, null=True, related_name='id_puerta_tarjeta')
    id_evento = models.ForeignKey(TbNevento, models.DO_NOTHING, db_column='id_evento',
                                  blank=True, null=True, related_name='id_evento_tarjeta')
    id_tarjeta = models.ForeignKey(
        TbDtarjetaAlimentacion, models.DO_NOTHING, db_column='id_tarjeta', blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'tb_dtarjeta_distribucion'


class TbNregla(models.Model):
    id_institucion = models.ForeignKey(TbInstitucion, models.CASCADE)
    id_regla = models.AutoField(primary_key=True)
    nombre_regla = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    descripcion_regla = models.TextField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'tb_nregla'


class TbDvaloresRegla(models.Model):
    id_institucion = models.ForeignKey(TbInstitucion, models.CASCADE)
    id_valores_regla = models.AutoField(primary_key=True)
    nombre_valores_regla = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    id_regla = models.ForeignKey(
        TbNregla, models.DO_NOTHING, db_column='id_regla', blank=True, null=True)
    # hay q  ver para q es este id y por que esta ahi sin relacion alguna
    id_valor_regla = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'tb_dvalores_regla'


class TbLastDistribucion(models.Model):
    id_institucion = models.ForeignKey(TbInstitucion, models.CASCADE)
    id_temp = models.AutoField(primary_key=True)
    id_persona = models.CharField(max_length=255, blank=True, null=True)
    id_usuario_registro = models.IntegerField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    fecha_modificacion = models.DateField(blank=True, null=True)
    id_usuario_modificacion = models.IntegerField(blank=True, null=True)
    id_distribucion = models.IntegerField(blank=True, null=True)
    id_complejo_comedor = models.IntegerField(blank=True, null=True)
    id_comedor = models.IntegerField(blank=True, null=True)
    id_puerta = models.IntegerField(blank=True, null=True)
    id_evento = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'tb_last_distribucion'


class TbNrangoEvento(models.Model):
    id_institucion = models.ForeignKey(TbInstitucion, models.CASCADE)
    id_rango_evento = models.AutoField(primary_key=True)
    activo = models.BooleanField(blank=True, null=True)
    descripcion_rango_evento = models.TextField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    hora_inicio = models.TimeField(blank=True, null=True)
    hora_fin = models.TimeField(blank=True, null=True)

    class Meta:
        db_table = 'tb_nrango_evento'


class TbRdistribucionRegla(models.Model):
    id_institucion = models.ForeignKey(TbInstitucion, models.CASCADE)
    id_distribucion_regla = models.AutoField(primary_key=True)
    id_distribucion = models.ForeignKey(
        TbDdistribucion, models.DO_NOTHING, db_column='id_distribucion', blank=True, null=True)
    nombre_regla = models.TextField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    nombre_valor_regla = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'tb_rdistribucion_regla'


class TbRestructuraRegla(models.Model):
    id_institucion = models.ForeignKey(TbInstitucion, models.CASCADE)
    id_estructura_regla = models.AutoField(primary_key=True)
    id_estructura = models.ForeignKey(
        TbStructure, models.DO_NOTHING, db_column='id_estructura', blank=True, null=True)
    id_regla = models.ForeignKey(
        TbNregla, models.DO_NOTHING, db_column='id_regla', blank=True, null=True)
    # por que esta este id asi sin relacion aqui ojo
    id_valor_regla = models.IntegerField(blank=True, null=True)
    nombre_valor_regla = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'tb_restructura_regla'


class TbReventoHorario(models.Model):
    id_institucion = models.ForeignKey(TbInstitucion, models.CASCADE)
    id_evento_horario = models.AutoField(primary_key=True)
    id_evento = models.ForeignKey(
        TbNevento, models.DO_NOTHING, db_column='id_evento')
    id_horario = models.ForeignKey(
        TbNhorario, models.DO_NOTHING, db_column='id_horario')

    class Meta:
        db_table = 'tb_revento_horario'


class TbReventoRangoEvento(models.Model):
    id_institucion = models.ForeignKey(TbInstitucion, models.CASCADE)
    id_evento_rango_evento = models.AutoField(primary_key=True)
    id_evento = models.ForeignKey(
        TbNevento, models.DO_NOTHING, db_column='id_evento', blank=True, null=True)
    id_rango_evento = models.ForeignKey(
        TbNrangoEvento, models.DO_NOTHING, db_column='id_rango_evento', blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    id_usuario_registro = models.ForeignKey(
        TbUser, models.DO_NOTHING, db_column='id_usuario_registro', blank=True, null=True)

    class Meta:
        db_table = 'tb_revento_rango_evento'

################################################################    Fin      #################################################################

################################################################ Esquema cajero ##############################################################


class TbDconfiguracionTarjeta(models.Model):
    id_institucion = models.ForeignKey(TbInstitucion, models.CASCADE)
    id_configuracion_tarjeta = models.AutoField(primary_key=True)
    id_tarjeta_alimentacion = models.ForeignKey(
        TbDtarjetaAlimentacion, models.DO_NOTHING, db_column='id_tarjeta_alimentacion', blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    id_complejo_comedor = models.ForeignKey(TbStructure, models.DO_NOTHING, db_column='id_complejo_comedor',
                                            blank=True, null=True, related_name='id_complejo_comedor_configuracionTarjeta')
    id_comedor = models.ForeignKey(TbStructure, models.DO_NOTHING, db_column='id_comedor',
                                   blank=True, null=True, related_name='id_comedor_configuracionTarjeta')
    id_puerta = models.ForeignKey(TbStructure, models.DO_NOTHING, db_column='id_puerta',
                                  blank=True, null=True, related_name='id_puerta_configuracionTarjeta')
    id_evento = models.ForeignKey(
        TbNevento, models.DO_NOTHING, db_column='id_evento', blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)

    class Meta:
        db_table = 'tb_dconfiguracion_tarjeta'


class TbNestadoMovimientoAsignacion(models.Model):
    id_institucion = models.ForeignKey(TbInstitucion, models.CASCADE)
    id_estado_movimiento_asignacion = models.AutoField(primary_key=True)
    nombre_estado_movimiento_asignacion = models.TextField()
    fecha_registro = models.DateField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)

    class Meta:
        db_table = 'tb_nestado_movimiento_asignacion'


class TbMovimientoAsignacion(models.Model):
    id_institucion = models.ForeignKey(TbInstitucion, models.CASCADE)
    id_movimiento_asignacion = models.AutoField(primary_key=True)
    id_puerta_origen = models.ForeignKey(TbStructure, models.DO_NOTHING, db_column='id_puerta_origen',
                                         blank=True, null=True, related_name='id_puerta_origen_MovimientoAsignacion')
    id_puerta_destino = models.ForeignKey(TbStructure, models.DO_NOTHING, db_column='id_puerta_destino',
                                          blank=True, null=True, related_name='id_puerta_destino_MovimientoAsignacion')
    id_evento = models.ForeignKey(
        TbNevento, models.DO_NOTHING, db_column='id_evento', blank=True, null=True)
    fecha_movimiento = models.DateField(blank=True, null=True)
    id_usuario_registro = models.ForeignKey(TbUser, models.DO_NOTHING, db_column='id_usuario_registro',
                                            blank=True, null=True, related_name='id_usuario_registro_MovimientoAsignacion')
    id_estado_movimiento_asignacion = models.ForeignKey(
        TbNestadoMovimientoAsignacion, models.DO_NOTHING, db_column='id_estado_movimiento_asignacion', blank=True, null=True)
    id_usuario_modificacion = models.ForeignKey(TbUser, models.DO_NOTHING, db_column='id_usuario_modificacion',
                                                blank=True, null=True, related_name='id_usuario_modificacion_MovimientoAsignacion')
    fecha_modificacion = models.DateField(blank=True, null=True)
    hora_movimiento_registro = models.TimeField(blank=True, null=True)
    hora_movimiento_modificacion = models.TimeField(blank=True, null=True)

    class Meta:
        db_table = 'tb_movimiento_asignacion'


class TbRpersonaTarjeta(models.Model):
    id_institucion = models.ForeignKey(TbInstitucion, models.CASCADE)
    id_persona_tarjeta = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey(
        TbDpersona, models.DO_NOTHING, db_column='id_persona', blank=True, null=True)
    id_tarjeta = models.ForeignKey(
        TbDtarjetaAlimentacion, models.DO_NOTHING, db_column='id_tarjeta', blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)

    class Meta:
        db_table = 'tb_rpersona_tarjeta'
########################################################################## Fin ###############################################################################
