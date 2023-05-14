from rest_framework import serializers
from .models import *

class TbNpaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNpais
        fields = '__all__'
    
class TbNprovinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNprovincia
        fields = '__all__'

class TbNtipoEstructuraSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNtipoEstructura
        fields = '__all__'

class TbNedificioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNedificio
        fields = '__all__'
       
class TbNestructuraSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNestructura
        fields = '__all__'

class TbNcategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNcategoria
        fields = '__all__'

class TbNaptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNapto
        fields = '__all__'

class TbNsexoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNsexo
        fields = '__all__'

class TbNcarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNcarrera
        fields = '__all__'

class TbNcategoriaResidenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNcategoriaResidente
        fields = '__all__'

class TbNgrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNgrupo
        fields = '__all__'
 
class TbNtipoCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNtipoCurso
        fields = '__all__'
        
class TbNcategoriaDocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNcategoriaDocente
        fields = '__all__'

class TbNorigenSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNorigen
        fields = '__all__'
    

class TbNmunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNmunicipio
        fields = '__all__'
    
class TbNresponsabilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNresponsabilidad
        fields = '__all__'
    
class TbNcategoriaCientificaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNcategoriaCientifica
        fields = '__all__'
    
class TbNparentescoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNparentesco
        fields = '__all__'
    
  
class TbDpersonaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbDpersona
        fields = '__all__'

class TbDpersonaSerializer(serializers.ModelSerializer):
    id_sexo = TbNsexoSerializer(read_only=True)
    id_municipio = TbNmunicipioSerializer(read_only=True)
    id_estructura = TbNestructuraSerializer(read_only=True)
    nombre_completo = models.CharField(max_length=255)
    id_categoria = TbNcategoriaSerializer(read_only=True)
    activo = models.BooleanField()
    id_estructura_credencial = TbNestructuraSerializer(read_only=True)
    id_persona_foto = models.CharField(max_length=36, blank=True, null=True)
    id_responsabilidad = TbNresponsabilidadSerializer(read_only=True)
    nombre_usuario = models.TextField(blank=True, null=True)
    nombre_responsabilidad = models.TextField(blank=True, null=True)
    id_estructura_consejo = TbNestructuraSerializer(read_only=True)
    id_categoria_residente = TbNcategoriaResidenteSerializer(read_only=True)
    id_tipo_curso = TbNtipoCursoSerializer(read_only=True)
    id_apto = TbNaptoSerializer(read_only=True)
    id_origen = TbNorigenSerializer(read_only=True)
    id_edificio = TbNedificioSerializer(read_only=True)
    id_carrera = TbNcarreraSerializer(read_only=True)
    id_pais = TbNpaisSerializer(read_only=True)
    id_categoria_cientifica = TbNcategoriaCientificaSerializer(read_only=True)
    id_categoria_docente = TbNcategoriaDocenteSerializer(read_only=True)
    id_grupo = TbNgrupoSerializer(read_only=True)  
    class Meta:
        model = TbDpersona
        fields = '__all__'
    
class TbRpersonaAkademosFamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbRpersonaAkademosFamiliar
        fields = '__all__'

class TbDpersonaTorpedoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbDpersonaTorpedo
        fields = '__all__'

class TbRpersonaFamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbRpersonaFamiliar
        fields = '__all__'

class TbTempIdPersonaTarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbTempIdPersonaTarjeta
        fields = '__all__'

class TbDpersonaFotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbDpersonaFoto
        fields = '__all__'
    