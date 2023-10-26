from django.db import models
from autenticacion.models.entities.usuario import Usuario
from base.models import  TbNcategoriaResidente, TbNcategoria
from cajero.models import TbNevento
from autenticacion.models.entities.institucion import Institucion


class TbNtipoCobro(models.Model):
    id_tipo_cobro = models.AutoField(primary_key=True)
    nombre_tipo_cobro = models.TextField()
    fecha_registro = models.DateField()
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    id_institucion = models.ForeignKey(Institucion, models.CASCADE)

    class Meta:
        verbose_name='Tipo de cobro'
        db_table = 'tb_ntipo_cobro'


class TbNconfiguracionCobro(models.Model):
    id_configuracion_cobro = models.AutoField(primary_key=True)
    nombre_configuracion_cobro = models.TextField()
    fecha_registro = models.DateField(auto_now=True,blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    id_institucion = models.ForeignKey(Institucion, models.CASCADE)

    def save(self, *args, **kwargs):
        if self.activo:
            # Desactivar todas las otras configuraciones
            TbNconfiguracionCobro.objects.exclude(pk=self.pk).update(activo=False)
        super(TbNconfiguracionCobro, self).save(*args, **kwargs)
    class Meta:
        db_table = 'tb_nconfiguracion_cobro'


class TbNvaloresConfiguracionCobro(models.Model):
    id_valores_configuracion_cobro = models.AutoField(primary_key=True)
    precio = models.FloatField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    id_categoria = models.ForeignKey(
        TbNcategoria, models.DO_NOTHING, db_column='id_categoria', blank=True, null=True)
    id_categoria_residente = models.ForeignKey(
        TbNcategoriaResidente, models.DO_NOTHING, db_column='id_categoria_residente', blank=True, null=True)
    id_evento = models.ForeignKey(
        TbNevento, models.DO_NOTHING, db_column='id_evento', blank=True, null=True)
    id_tipo_cobro = models.ForeignKey(
        TbNtipoCobro, models.DO_NOTHING, db_column='id_tipo_cobro', blank=True, null=True)
    id_configuracion_cobro = models.ForeignKey(
        TbNconfiguracionCobro, models.DO_NOTHING, db_column='id_configuracion_cobro', blank=True, null=True)
    id_institucion = models.ForeignKey(Institucion, models.CASCADE)

    class Meta:
        db_table = 'tb_nvalores_configuracion_cobro'



