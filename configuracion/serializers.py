from rest_framework import serializers
from .models import *
from autenticacion.gateway.serializers.usuario.v1.lectura import SerializadorDeUsuarioLecturaConPerfil
from base.serializers import (TbNcategoriaResidenteSerializer, TbNcategoriaSerializer, TbNestructuraSerializer,
                              TbNtipoCursoSerializer)


class TbDconfiguracionPersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbDconfiguracionPersona
        fields = '__all__'


class TbDconfiguracionProcesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbDconfiguracionProceso
        fields = '__all__'


class TbDconfiguracionProcesoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbDconfiguracionProceso
        fields = '__all__'


class TbDdatosContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbDdatosContacto
        fields = '__all__'


class TbDvaloresConfiguracionPersonaSerializer(serializers.ModelSerializer):
    id_configuracion_persona = TbDconfiguracionPersonaSerializer(
        read_only=True)
    id_categoria = TbNcategoriaSerializer(read_only=True)
    id_categoria_residente = TbNcategoriaResidenteSerializer(read_only=True)
    id_estructura = TbNestructuraSerializer(read_only=True)
    id_tipo_curso = TbNtipoCursoSerializer(read_only=True)

    class Meta:
        model = TbDvaloresConfiguracionPersona
        fields = '__all__'


class TbDvaloresConfiguracionPersonaCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbDvaloresConfiguracionPersona
        fields = '__all__'
