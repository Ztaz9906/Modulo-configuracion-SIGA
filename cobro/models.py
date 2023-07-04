from django.db import models
from adminschema.models import TbUser
from base.models import TbDpersona, TbNcategoriaResidente, TbNcategoria
from cajero.models import TbNevento


class TbTipoRegla(models.Model):
    id_tipo_regla = models.AutoField(primary_key=True)
    nombre_tipo_regla = models.TextField()
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)

    class Meta:

        db_table = 'tb_tipo_regla'


class TbNestadoImportacion(models.Model):
    id_estado_importacion = models.AutoField(primary_key=True)
    nombre_estado_importacion = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)

    class Meta:

        db_table = 'tb_nestado_importacion'


class TbDimportacion(models.Model):
    id_importacion = models.AutoField(primary_key=True)
    nombre_importacion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    id_estado_importacion = models.ForeignKey(
        TbNestadoImportacion, models.DO_NOTHING, db_column='id_estado_importacion', blank=True, null=True)
    id_usuario_registro = models.ForeignKey(TbUser, models.DO_NOTHING, db_column='id_usuario_registro',
                                            blank=True, null=True, related_name='id_usuario_registro_importacion')
    id_usuario_modificacion = models.ForeignKey(
        TbUser, models.DO_NOTHING, db_column='id_usuario_modificacion', blank=True, null=True, related_name='id_usuario_modificacion_importacion')
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:

        db_table = 'tb_dimportacion'


class TbDimportaciones(models.Model):
    id_importacion = models.AutoField(primary_key=True)
    nombre_importacion = models.TextField()
    activo = models.BooleanField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    id_usuario_registro = models.ForeignKey(TbUser, models.DO_NOTHING, db_column='id_usuario_registro',
                                            blank=True, null=True, related_name='id_usuario_registro_importaciones')
    fecha_registro = models.DateField()
    importe_desayuno = models.FloatField(blank=True, null=True)
    importe_doble_desayuno = models.FloatField(blank=True, null=True)
    importe_almuerzo = models.FloatField(blank=True, null=True)
    importe_doble_almuerzo = models.FloatField(blank=True, null=True)
    importe_comida = models.FloatField(blank=True, null=True)
    importe_doble_comida = models.FloatField(blank=True, null=True)

    class Meta:

        db_table = 'tb_dimportaciones'


class TbDimportacionRegistro(models.Model):
    id_importacion_registro = models.AutoField(primary_key=True)
    # Por que no tiene relacion con la tabla persona en la base de datos
    id_persona = models.CharField(max_length=255)
    id_importacion = models.ForeignKey(
        TbDimportaciones, models.DO_NOTHING, db_column='id_importacion')
    importe_reservaciones = models.FloatField(blank=True, null=True)
    # This field type is a guess. revisar aqui tambien
    id_familiar = models.TextField(blank=True, null=True)

    class Meta:

        db_table = 'tb_dimportacion_registro'


class TbDpersonaRegla(models.Model):
    id_persona_regla = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey(
        TbDpersona, models.DO_NOTHING, db_column='id_persona', blank=True, null=True)
    activo = models.BooleanField()
    # This field type is a guess.
    reglas = models.TextField(blank=True, null=True)

    class Meta:

        db_table = 'tb_dpersona_regla'


class TbDreglaCobro(models.Model):
    id_regla_cobro = models.AutoField(primary_key=True)
    nombre_regla_cobro = models.TextField()
    id_usuario_registro = models.ForeignKey(TbUser, models.DO_NOTHING, db_column='id_usuario_registro',
                                            blank=True, null=True, related_name='id_usuario_registro_reglaCobro')
    activo = models.BooleanField()
    fijo = models.BooleanField()
    fecha_registro = models.DateField(blank=True, null=True)
    # This field type is a guess.
    eventos_afectados = models.TextField(blank=True, null=True)
    # This field type is a guess.
    dias_afectados = models.TextField(blank=True, null=True)
    id_tipo_regla = models.ForeignKey(
        TbTipoRegla, models.DO_NOTHING, db_column='id_tipo_regla', blank=True, null=True)
    descripcion = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:

        db_table = 'tb_dregla_cobro'


class TbNtipoCobro(models.Model):
    id_tipo_cobro = models.AutoField(primary_key=True)
    nombre_tipo_cobro = models.TextField()
    fecha_registro = models.DateField()
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)

    class Meta:

        db_table = 'tb_ntipo_cobro'


class TbRfechaExcluida(models.Model):
    id_fecha_excluida = models.AutoField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    id_categoria_residente = models.ForeignKey(
        TbNcategoriaResidente, models.DO_NOTHING, db_column='id_categoria_residente', blank=True, null=True)
    id_categoria = models.ForeignKey(
        TbNcategoria, models.DO_NOTHING, db_column='id_categoria', blank=True, null=True)
    id_evento = models.ForeignKey(
        TbNevento, models.DO_NOTHING, db_column='id_evento', blank=True, null=True)

    class Meta:

        db_table = 'tb_rfecha_excluida'


class TbRimportacionReservacion(models.Model):
    id_importacion_reservacion = models.AutoField(primary_key=True)
    id_importacion = models.ForeignKey(
        TbDimportacion, models.DO_NOTHING, db_column='id_importacion', blank=True, null=True)
    # id_reservacion = models.ForeignKey(
    #     TbDreservacion, models.DO_NOTHING, db_column='id_reservacion', blank=True, null=True)

    class Meta:

        db_table = 'tb_rimportacion_reservacion'


class TbRpersonaExcluidaCobro(models.Model):
    id_persona_excluida_cobro = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey(
        TbDpersona, models.DO_NOTHING, db_column='id_persona', blank=True, null=True)
    id_importacion = models.ForeignKey(
        TbDimportacion, models.DO_NOTHING, db_column='id_importacion', blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    id_usuario_registro = models.ForeignKey(TbUser, models.DO_NOTHING, db_column='id_usuario_registro',
                                            blank=True, null=True, related_name='id_usuario_registro_personaExcluidaCobro')

    class Meta:

        db_table = 'tb_rpersona_excluida_cobro'
