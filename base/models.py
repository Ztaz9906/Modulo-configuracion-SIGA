from django.db import models
from adminschema.models import TbUser


class TbNpais(models.Model):
    nombre_pais = models.CharField(max_length=255)
    fecha_registro_pais = models.DateTimeField()
    descripcion_pais = models.TextField(blank=True, null=True)
    activo = models.BooleanField()
    id_pais = models.CharField(primary_key=True, max_length=3)

    class Meta:

        db_table = 'tb_npais'


class TbNprovincia(models.Model):
    id_provincia = models.IntegerField(primary_key=True)
    nombre_provincia = models.CharField(max_length=255)
    fecha_registro_provincia = models.DateTimeField()
    descripcion_provincia = models.TextField(blank=True, null=True)
    codigo_oficial_provincia = models.CharField(max_length=255)
    activo = models.BooleanField()
    abreviatura = models.CharField(max_length=255, blank=True, null=True)
    id_pais = models.ForeignKey(
        TbNpais, models.DO_NOTHING, db_column='id_pais')

    class Meta:

        db_table = 'tb_nprovincia'


class TbNtipoEstructura(models.Model):
    id_tipo_estructura = models.IntegerField(primary_key=True)
    id_tipo_estructura_padre = models.IntegerField(blank=True, null=True)
    nombre_tipo_estructura = models.CharField(max_length=255)
    fecha_registro_tipo_estructura = models.DateTimeField()
    descripcion_tipo_estructura = models.TextField(blank=True, null=True)
    activo = models.BooleanField()

    class Meta:

        db_table = 'tb_ntipo_estructura'


class TbNedificio(models.Model):
    id_edificio = models.AutoField(primary_key=True)
    nombre_edificio = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    descripcion_edificio = models.TextField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)

    class Meta:

        db_table = 'tb_nedificio'


class TbNestructura(models.Model):
    id_estructura = models.IntegerField(primary_key=True)
    id_tipo_estructura = models.ForeignKey(
        TbNtipoEstructura, models.DO_NOTHING, db_column='id_tipo_estructura', blank=True, null=True)
    id_estructura_padre = models.IntegerField(blank=True, null=True)
    nombre_estructura = models.CharField(max_length=255)
    codigo_externo = models.CharField(max_length=255)
    codigo_area = models.CharField(max_length=255)
    estructura_consejo = models.BooleanField(blank=True, null=True)
    estructura_credencial = models.BooleanField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)

    class Meta:

        db_table = 'tb_nestructura'


class TbNcategoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre_categoria = models.CharField(max_length=255)
    fecha_registro_categoria = models.DateTimeField()
    descripcion_categoria = models.TextField(blank=True, null=True)
    activo = models.BooleanField()

    class Meta:

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

        db_table = 'tb_napto'


class TbNsexo(models.Model):
    id_sexo = models.IntegerField(primary_key=True)
    nombre_sexo = models.CharField(max_length=255)
    fecha_registro_sexo = models.DateTimeField()
    descripcion_sexo = models.TextField(blank=True, null=True)
    activo = models.BooleanField()

    class Meta:

        db_table = 'tb_nsexo'


class TbNcarrera(models.Model):
    id_carrera = models.AutoField(primary_key=True)
    nombre_carrera = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    descripcion_carrera = models.TextField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)

    class Meta:

        db_table = 'tb_ncarrera'


class TbNcategoriaResidente(models.Model):
    id_categoria_residente = models.AutoField(primary_key=True)
    nombre_categoria_residente = models.TextField()
    fecha_registro = models.DateField()
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField()
    siglas = models.TextField(blank=True, null=True)

    class Meta:

        db_table = 'tb_ncategoria_residente'


class TbNgrupo(models.Model):
    id_grupo = models.AutoField(primary_key=True)
    nombre_grupo = models.CharField(max_length=255)
    fecha_registro = models.DateField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)

    class Meta:

        db_table = 'tb_ngrupo'


class TbNtipoCurso(models.Model):
    id_tipo_curso = models.AutoField(primary_key=True)
    nombre_tipo_curso = models.CharField(max_length=255)
    fecha_registro = models.DateField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)

    class Meta:

        db_table = 'tb_ntipo_curso'


class TbNcategoriaDocente(models.Model):
    id_categoria_docente = models.AutoField(primary_key=True)
    nombre_categoria_docente = models.CharField(max_length=255)
    fecha_registro = models.DateField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)

    class Meta:

        db_table = 'tb_ncategoria_docente'


class TbNorigen(models.Model):
    id_origen = models.AutoField(primary_key=True)
    nombre_origen = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    descripcion_origen = models.TextField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)

    class Meta:

        db_table = 'tb_norigen'


class TbNmunicipio(models.Model):
    id_municipio = models.IntegerField(primary_key=True)
    id_provincia = models.ForeignKey(
        TbNprovincia, models.DO_NOTHING, db_column='id_provincia', blank=True, null=True)
    nombre_municipio = models.CharField(max_length=255)
    fecha_registro_municipio = models.DateTimeField()
    descripcion_municipio = models.TextField(blank=True, null=True)
    activo = models.BooleanField()
    codigo_oficial_municipio = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'tb_nmunicipio'


class TbNresponsabilidad(models.Model):
    id_responsabilidad = models.AutoField(primary_key=True)
    nombre_responsabilidad = models.CharField(max_length=255)
    fecha_registro_responsabilidad = models.DateTimeField()
    descripcion_responsabilidad = models.TextField(blank=True, null=True)
    activo = models.BooleanField()

    class Meta:

        db_table = 'tb_nresponsabilidad'


class TbNcategoriaCientifica(models.Model):
    id_categoria_cientifica = models.AutoField(primary_key=True)
    nombre_categoria_cientifica = models.CharField(max_length=255)
    fecha_registro = models.DateField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)

    class Meta:

        db_table = 'tb_ncategoria_cientifica'


class TbNparentesco(models.Model):
    activo = models.BooleanField(blank=True, null=True)
    id_parentesco = models.IntegerField(primary_key=True)
    nombre_parentesco = models.CharField(max_length=255, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    descripcion_parentesco = models.CharField(
        max_length=255, blank=True, null=True)

    class Meta:

        db_table = 'tb_nparentesco'


class TbDpersona(TbUser):
    id_persona = models.CharField(primary_key=True, max_length=255)
    id_sexo = models.ForeignKey(
        TbNsexo, models.DO_NOTHING, db_column='id_sexo', blank=True, null=True)
    id_municipio = models.ForeignKey(
        TbNmunicipio, models.DO_NOTHING, db_column='id_municipio', blank=True, null=True)
    id_estructura = models.ForeignKey(TbNestructura, models.DO_NOTHING, db_column='id_estructura',
                                      blank=True, null=True, related_name='id_estructura_persona')
    nombre_completo = models.CharField(max_length=255)
    ci = models.CharField(max_length=255)
    solapin = models.CharField(max_length=255, blank=True, null=True)
    id_expediente = models.CharField(max_length=255, blank=True, null=True)
    id_categoria = models.ForeignKey(
        TbNcategoria, models.DO_NOTHING, db_column='id_categoria', blank=True, null=True)
    activo = models.BooleanField()
    id_estructura_credencial = models.ForeignKey(
        TbNestructura, models.DO_NOTHING, db_column='id_estructura_credencial', blank=True, null=True, related_name='id_estructura_credencial_persona')
    id_persona_foto = models.CharField(max_length=36, blank=True, null=True)
    id_responsabilidad = models.ForeignKey(
        TbNresponsabilidad, models.DO_NOTHING, db_column='id_responsabilidad', blank=True, null=True)
    nombre_responsabilidad = models.TextField(blank=True, null=True)
    id_estructura_consejo = models.ForeignKey(TbNestructura, models.DO_NOTHING, db_column='id_estructura_consejo',
                                              blank=True, null=True, related_name='id_estructura_consejo_persona')
    id_categoria_residente = models.ForeignKey(
        TbNcategoriaResidente, models.DO_NOTHING, db_column='id_categoria_residente', blank=True, null=True)
    id_tipo_curso = models.ForeignKey(
        TbNtipoCurso, models.DO_NOTHING, db_column='id_tipo_curso', blank=True, null=True)
    id_apto = models.ForeignKey(
        TbNapto, models.DO_NOTHING, db_column='id_apto', blank=True, null=True)
    id_origen = models.ForeignKey(
        TbNorigen, models.DO_NOTHING, db_column='id_origen', blank=True, null=True)
    codigo_solapin = models.CharField(max_length=1, blank=True, null=True)
    id_edificio = models.ForeignKey(
        TbNedificio, models.DO_NOTHING, db_column='id_edificio', blank=True, null=True)
    id_carrera = models.ForeignKey(
        TbNcarrera, models.DO_NOTHING, db_column='id_carrera', blank=True, null=True)
    id_pais = models.ForeignKey(
        TbNpais, models.DO_NOTHING, db_column='id_pais', blank=True, null=True)
    id_categoria_cientifica = models.ForeignKey(
        TbNcategoriaCientifica, models.DO_NOTHING, db_column='id_categoria_cientifica', blank=True, null=True)
    id_categoria_docente = models.ForeignKey(
        TbNcategoriaDocente, models.DO_NOTHING, db_column='id_categoria_docente', blank=True, null=True)
    id_grupo = models.ForeignKey(
        TbNgrupo, models.DO_NOTHING, db_column='id_grupo', blank=True, null=True)

    class Meta:
        db_table = 'tb_dpersona'


class TbDpersonaTorpedo(TbUser):
    id_persona_torpedo = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=255)
    ci = models.CharField(max_length=255)
    id_sexo = models.ForeignKey(
        TbNsexo, models.DO_NOTHING, db_column='id_sexo', blank=True, null=True)
    activo = models.BooleanField()
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
        db_table = 'tb_dpersona_torpedo'


class TbRpersonaFamiliar(models.Model):
    id_persona_familiar = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey(TbDpersona, models.DO_NOTHING, db_column='id_persona',
                                   blank=True, null=True, related_name='id_persona_personaFamiliar')
    id_familiar = models.ForeignKey(TbDpersona, models.DO_NOTHING, db_column='id_familiar',
                                    blank=True, null=True, related_name='id_familiar_personaFamiliar')
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
