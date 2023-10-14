from django.db import models
from autenticacion.models.entities.institucion import Institucion
class TbNpais(models.Model):
    nombre_pais = models.CharField(max_length=255)
    fecha_registro_pais = models.DateTimeField()
    descripcion_pais = models.TextField(blank=True, null=True)
    activo = models.BooleanField()
    id_pais = models.AutoField(primary_key=True)
    class Meta:
        verbose_name = "Pais"
        verbose_name_plural = "Paises"
        db_table = 'tb_npais'

class TbNprovincia(models.Model):
    id_provincia = models.AutoField(primary_key=True)
    nombre_provincia = models.CharField(max_length=255)
    fecha_registro_provincia = models.DateTimeField()
    descripcion_provincia = models.TextField(blank=True, null=True)
    codigo_oficial_provincia = models.CharField(max_length=255)
    activo = models.BooleanField()
    abreviatura = models.CharField(max_length=255, blank=True, null=True)
    id_pais = models.ForeignKey(
        TbNpais, models.DO_NOTHING, db_column='id_pais')

    class Meta:
        verbose_name = "Provincia"
        verbose_name_plural = "Provincias"
        db_table = 'tb_nprovincia'

class TbNtipoEstructura(models.Model):
    id_tipo_estructura = models.AutoField(primary_key=True)
    id_institucion = models.ForeignKey(
        Institucion, on_delete=models.CASCADE, null=True, blank=True)
    nombre_tipo_estructura = models.CharField(max_length=255)
    fecha_registro_tipo_estructura = models.DateTimeField()
    descripcion_tipo_estructura = models.TextField(blank=True, null=True)
    activo = models.BooleanField()

    class Meta:
        verbose_name = "Tipo Estructura"
        verbose_name_plural = "Tipo Estructuras"
        db_table = 'tb_ntipo_estructura'

class TbNedificio(models.Model):
    id_edificio = models.AutoField(primary_key=True)
    nombre_edificio = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    descripcion_edificio = models.TextField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = "Edificio"
        verbose_name_plural = "Edificios"
        db_table = 'tb_nedificio'

class TbNestructura(models.Model):
    id_estructura = models.AutoField(primary_key=True)
    id_tipo_estructura = models.ForeignKey(
            TbNtipoEstructura, models.DO_NOTHING, db_column='id_tipo_estructura', blank=True, null=True)
    id_institucion = models.ForeignKey(
        Institucion, on_delete=models.CASCADE, null=True, blank=True)
    nombre_estructura = models.CharField(max_length=255)
    codigo_externo = models.CharField(max_length=255)
    codigo_area = models.CharField(max_length=255)
    estructura_consejo = models.BooleanField(blank=True, null=True)
    estructura_credencial = models.BooleanField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)

    class Meta:
        verbose_name = "Estructura"
        verbose_name_plural = "Estructuras"
        db_table = 'tb_nestructura'

class TbNcategoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=255)
    fecha_registro_categoria = models.DateTimeField()
    descripcion_categoria = models.TextField(blank=True, null=True)
    activo = models.BooleanField()

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        db_table = 'tb_ncategoria'

class TbNapto(models.Model):
    id_apto = models.AutoField(primary_key=True)
    nombre_apto = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    descripcion_apto = models.TextField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    id_edificio = models.ForeignKey(
        TbNedificio, models.DO_NOTHING, db_column='id_edificio', blank=True, null=True)

    class Meta:
        verbose_name = "Apartamento"
        verbose_name_plural = "Apartamentos"
        db_table = 'tb_napto'

class TbNsexo(models.Model):
    id_sexo = models.AutoField(primary_key=True)
    nombre_sexo = models.CharField(max_length=255)
    fecha_registro_sexo = models.DateTimeField()
    descripcion_sexo = models.TextField(blank=True, null=True)
    activo = models.BooleanField()

    class Meta:
        verbose_name = "Sexo"
        verbose_name_plural = "Sexos"
        db_table = 'tb_nsexo'

class TbNcarrera(models.Model):
    id_carrera = models.AutoField(primary_key=True)
    nombre_carrera = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    descripcion_carrera = models.TextField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = "Carrera"
        verbose_name_plural = "Carreras"
        db_table = 'tb_ncarrera'

class TbNcategoriaResidente(models.Model):
    id_categoria_residente = models.AutoField(primary_key=True)
    nombre_categoria_residente = models.TextField()
    fecha_registro = models.DateField()
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField()
    siglas = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Categorias Residente"
        verbose_name_plural = "Categorias Residentes"
        db_table = 'tb_ncategoria_residente'

class TbNgrupo(models.Model):
    id_grupo = models.AutoField(primary_key=True)
    nombre_grupo = models.CharField(max_length=255)
    fecha_registro = models.DateField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)

    class Meta:
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"
        db_table = 'tb_ngrupo'

class TbNtipoCurso(models.Model):
    id_tipo_curso = models.AutoField(primary_key=True)
    nombre_tipo_curso = models.CharField(max_length=255)
    fecha_registro = models.DateField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)

    class Meta:
        verbose_name = "Tipo de curso"
        verbose_name_plural = "Tipo de cursos"
        db_table = 'tb_ntipo_curso'

class TbNcategoriaDocente(models.Model):
    id_categoria_docente = models.AutoField(primary_key=True)
    nombre_categoria_docente = models.CharField(max_length=255)
    fecha_registro = models.DateField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)

    class Meta:
        verbose_name = "Categorias Docente"
        verbose_name_plural = "Categorias Docentes"
        db_table = 'tb_ncategoria_docente'

class TbNorigen(models.Model):
    id_origen = models.AutoField(primary_key=True)
    nombre_origen = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    descripcion_origen = models.TextField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = "Origen"
        verbose_name_plural = "Origenes"
        db_table = 'tb_norigen'

class TbNmunicipio(models.Model):
    id_municipio = models.AutoField(primary_key=True)
    id_provincia = models.ForeignKey(
        TbNprovincia, models.DO_NOTHING, db_column='id_provincia', blank=True, null=True)
    nombre_municipio = models.CharField(max_length=255)
    fecha_registro_municipio = models.DateTimeField()
    descripcion_municipio = models.TextField(blank=True, null=True)
    activo = models.BooleanField()
    codigo_oficial_municipio = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"
        db_table = 'tb_nmunicipio'


class TbNresponsabilidad(models.Model):
    id_responsabilidad = models.AutoField(primary_key=True)
    nombre_responsabilidad = models.CharField(max_length=255)
    fecha_registro_responsabilidad = models.DateTimeField()
    descripcion_responsabilidad = models.TextField(blank=True, null=True)
    activo = models.BooleanField()

    class Meta:
        verbose_name = "Responsabilidad"
        verbose_name_plural = "Responsabilidades"
        db_table = 'tb_nresponsabilidad'


class TbNcategoriaCientifica(models.Model):
    id_categoria_cientifica = models.AutoField(primary_key=True)
    nombre_categoria_cientifica = models.CharField(max_length=255)
    fecha_registro = models.DateField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)

    class Meta:
        verbose_name = "Categorias Cientifica"
        verbose_name_plural = "Categorias Cientificas"
        db_table = 'tb_ncategoria_cientifica'


class TbNparentesco(models.Model):
    activo = models.BooleanField(blank=True, null=True)
    id_parentesco = models.AutoField(primary_key=True)
    nombre_parentesco = models.CharField(max_length=255, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    descripcion_parentesco = models.CharField(
        max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Parentesco"
        verbose_name_plural = "Parentescos"
        db_table = 'tb_nparentesco'



class TbRpersonaFamiliar(models.Model):
    id_persona_familiar = models.AutoField(primary_key=True)
    activo = models.BooleanField(blank=True, null=True)
    id_parentesco = models.ForeignKey(
        TbNparentesco, models.DO_NOTHING, db_column='id_parentesco', blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)

    class Meta:

        db_table = 'tb_rpersona_familiar'


class TbTempIdPersonaTarjeta(models.Model):
    id_temp = models.AutoField(primary_key=True)
    id_persona = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'tb_temp_id_persona_tarjeta'
