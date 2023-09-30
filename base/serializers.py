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

    class Meta:
        model = TbDpersona
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
