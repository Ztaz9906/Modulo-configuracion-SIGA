from rest_framework import serializers
from .models import *
from autenticacion.gateway.serializers.usuario.v1.lectura import SerializadorDeUsuarioLecturaConPerfil
from base.serializers import TbDpersonaSerializer, TbNestructuraSerializer


class TbDelementosMostrarSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbDelementosMostrar
        fields = '__all__'


class TbDperiodoReservacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbDperiodoReservacion
        fields = '__all__'


class TbDresponsableAreaPersonasSerializer(serializers.ModelSerializer):
    id_persona = TbDpersonaSerializer(read_only=True)
    id_estructura = TbNestructuraSerializer(read_only=True)
    id_persona_registro = SerializadorDeUsuarioLecturaConPerfil(read_only=True)

    class Meta:
        model = TbDresponsableAreaPersonas
        fields = '__all__'


class TbDresponsableAreaPersonasCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbDresponsableAreaPersonas
        fields = '__all__'


class TbDresponsableReservacionSerializer(serializers.ModelSerializer):
    id_persona = TbDpersonaSerializer(read_only=True)
    id_estructura = TbNestructuraSerializer(read_only=True)
    id_persona_registro = SerializadorDeUsuarioLecturaConPerfil(read_only=True)

    class Meta:
        model = TbDresponsableReservacion
        fields = '__all__'


class TbDresponsableReservacionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbDresponsableReservacion
        fields = '__all__'

# por que esta tabla no tiene relacion con ninguna en la base de datos revisar


class TbHistorialReservacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbHistorialReservacion
        fields = '__all__'
