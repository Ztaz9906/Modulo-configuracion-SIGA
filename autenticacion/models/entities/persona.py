from django.db import models
from autenticacion.models.entities.institucion import Institucion
from autenticacion.models.entities.configuracion_comensales import TbDconfiguracionPersona
from base.models import *
from django.contrib import admin
class Persona(models.Model):
    """Representa una persona."""
    nombre_completo = models.CharField(max_length=255, blank=True, null=True)
    ci = models.CharField(max_length=255, blank=True, null=True)
    solapin = models.CharField(max_length=255, blank=True, null=True)
    codigo_solapin = models.CharField(max_length=255, blank=True, null=True)
    nombre_responsabilidad = models.TextField(blank=True, null=True)
    id_expediente = models.CharField(max_length=255, blank=True, null=True)
    institucion = models.ForeignKey(
        Institucion, on_delete=models.CASCADE, null=True, blank=True)
    id_sexo = models.ForeignKey(
        TbNsexo, models.DO_NOTHING, db_column='id_sexo', blank=True, null=True)
    id_municipio = models.ForeignKey(
        TbNmunicipio, models.DO_NOTHING, db_column='id_municipio', blank=True, null=True)
    id_provincia = models.ForeignKey(
        TbNprovincia, models.DO_NOTHING, db_column='id_provincia', blank=True, null=True)
    id_responsabilidad = models.ForeignKey(
        TbNresponsabilidad, models.DO_NOTHING, db_column='id_responsabilidad', blank=True, null=True)
    id_apto = models.ForeignKey(
        TbNapto, models.DO_NOTHING, db_column='id_apto', blank=True, null=True)
    id_edificio = models.ForeignKey(
        TbNedificio, models.DO_NOTHING, db_column='id_edificio', blank=True, null=True)
    id_carrera = models.ForeignKey(
        TbNcarrera, models.DO_NOTHING, db_column='id_carrera', blank=True, null=True)
    id_pais = models.ForeignKey(
        TbNpais, models.DO_NOTHING, db_column='id_pais', blank=True, null=True)
    id_grupo = models.ForeignKey(
        TbNgrupo, models.DO_NOTHING, db_column='id_grupo', blank=True, null=True)
    id_estructura = models.ForeignKey(TbNestructura, models.DO_NOTHING, db_column='id_estructura',
                                      blank=True, null=True, related_name='id_estructura_persona')
    id_categoria = models.ForeignKey(
        TbNcategoria, models.DO_NOTHING, db_column='id_categoria', blank=True, null=True)
    id_categoria_cientifica = models.ForeignKey(
        TbNcategoriaCientifica, models.DO_NOTHING, db_column='id_categoria_cientifica', blank=True, null=True)
    id_categoria_docente = models.ForeignKey(
        TbNcategoriaDocente, models.DO_NOTHING, db_column='id_categoria_docente', blank=True, null=True)
    id_categoria_residente = models.ForeignKey(
        TbNcategoriaResidente, models.DO_NOTHING, db_column='id_categoria_residente', blank=True, null=True)
    id_configuracion_comensal = models.ForeignKey(TbDconfiguracionPersona,models.DO_NOTHING,db_column='id_configuracion_comensal', blank=True, null=True)

    def __str__(self) -> str:
        return self.nombre_completo

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    class Admin(admin.ModelAdmin):
        list_display = ["id", "nombre_completo","ci"]