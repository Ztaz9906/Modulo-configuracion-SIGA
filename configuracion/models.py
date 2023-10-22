from django.db import models
from autenticacion.models.entities.usuario import Usuario
from base.models import TbNcategoria, TbNcategoriaResidente, TbNestructura, TbNtipoCurso
from autenticacion.models.entities.institucion import Institucion
from autenticacion.models.entities.configuracion_comensales import TbDconfiguracionPersona


class TbDconfiguracionProceso(models.Model):
    id_institucion = models.ForeignKey(Institucion, models.CASCADE)
    id_configuracion_proceso = models.AutoField(primary_key=True)
    flujo = models.BooleanField(blank=True, null=True)
    descripcion_configuracion_proceso = models.TextField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    id_usuario_registro = models.ForeignKey(
        Usuario, models.DO_NOTHING, db_column='id_usuario_registro')

    class Meta:

        db_table = 'tb_dconfiguracion_proceso'


class TbDdatosContacto(models.Model):
    id_institucion = models.ForeignKey(Institucion, models.CASCADE)
    id_datos_contacto = models.AutoField(primary_key=True)
    direccion = models.TextField(blank=True, null=True)
    telefono = models.TextField(blank=True, null=True)
    correo = models.TextField(blank=True, null=True)
    id_usuario_registro = models.ForeignKey(
        Usuario, models.DO_NOTHING, db_column='id_usuario_registro',blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)

    class Meta:

        db_table = 'tb_ddatos_contacto'


class TbDvaloresConfiguracionPersona(models.Model):
    id_calores_configuracion_persona = models.AutoField(primary_key=True)
    id_institucion = models.ForeignKey(Institucion, models.CASCADE)
    id_configuracion_persona = models.ForeignKey(
        TbDconfiguracionPersona, models.DO_NOTHING, db_column='id_configuracion_persona', blank=True, null=True)
    id_categoria = models.ForeignKey(
        TbNcategoria, models.DO_NOTHING, db_column='id_categoria', blank=True, null=True)
    id_categoria_residente = models.ForeignKey(
        TbNcategoriaResidente, models.DO_NOTHING, db_column='id_categoria_residente', blank=True, null=True)
    id_estructura = models.ForeignKey(
        TbNestructura, models.DO_NOTHING, db_column='id_estructura', blank=True, null=True)
    id_tipo_curso = models.ForeignKey(
        TbNtipoCurso, models.DO_NOTHING, db_column='id_tipo_curso', blank=True, null=True)

    class Meta:

        db_table = 'tb_dvalores_configuracion_persona'
