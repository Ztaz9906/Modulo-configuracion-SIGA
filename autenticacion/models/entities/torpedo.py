from autenticacion.models.entities.institucion import Institucion
from base.models import *
from django.contrib import admin

class TbDpersonaTorpedo(models.Model):
    id_institucion = models.ForeignKey(
        Institucion, on_delete=models.CASCADE, null=True, blank=True)
    id_persona_torpedo = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=255)
    ci = models.CharField(max_length=255)
    id_sexo = models.ForeignKey(
        TbNsexo, models.DO_NOTHING, db_column='id_sexo', blank=True, null=True)
    id_municipio = models.ForeignKey(
        TbNmunicipio, models.DO_NOTHING, db_column='id_municipio', blank=True, null=True)
    id_provincia = models.ForeignKey(
        TbNprovincia, models.DO_NOTHING, db_column='id_provincia', blank=True, null=True)
    id_pais = models.ForeignKey(
        TbNpais, models.DO_NOTHING, db_column='id_pais', blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    id_usuario_registro = models.IntegerField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    fecha_actualizacion = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = "Torpedo"
        verbose_name_plural = "Torpedos"

    def __str__(self) -> str:
        return self.nombre_completo

    class Admin(admin.ModelAdmin):
        list_display = ["id_persona_torpedo", "nombre_completo", "ci", "id_institucion"]
