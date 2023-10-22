from rest_framework import serializers
from .models import *
from base.serializers import TbNcategoriaResidenteSerializer, TbNcategoriaSerializer
from cajero.serializerGet import TbNeventoSerializer


class TbNtipoCobroSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNtipoCobro
        fields = '__all__'


class TbNconfiguracionCobroSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNconfiguracionCobro
        fields = '__all__'


class TbNvaloresConfiguracionCobroSerializer(serializers.ModelSerializer):
    id_categoria = TbNcategoriaSerializer(read_only=True)
    id_categoria_residente = TbNcategoriaResidenteSerializer(read_only=True)
    id_evento = TbNeventoSerializer(read_only=True)
    id_tipo_cobro = TbNtipoCobroSerializer(read_only=True)
    id_configuracion_cobro = TbNconfiguracionCobroSerializer(read_only=True)

    class Meta:
        model = TbNvaloresConfiguracionCobro
        fields = '__all__'


class TbNvaloresConfiguracionCobroCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNvaloresConfiguracionCobro
        fields = '__all__'