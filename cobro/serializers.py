from rest_framework import serializers
from .models import *
from adminschema.serializer import TbUserSerializer
from base.serializers import TbDpersonaSerializer, TbNcategoriaResidenteSerializer, TbNcategoriaSerializer
from cajero.serializerGet import TbNeventoSerializer


class TbTipoReglaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbTipoRegla
        fields = '__all__'


class TbNestadoImportacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNestadoImportacion
        fields = '__all__'


class TbDimportacionSerializer(serializers.ModelSerializer):
    id_estado_importacion = TbNestadoImportacionSerializer(read_only=True)
    id_usuario_registro = TbUserSerializer(read_only=True)
    id_usuario_modificacion = TbUserSerializer(read_only=True)

    class Meta:
        model = TbDimportacion
        fields = '__all__'


class TbDimportacionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbDimportacion
        fields = '__all__'


class TbDimportacionesSerializer(serializers.ModelSerializer):
    id_usuario_registro = TbUserSerializer(read_only=True)

    class Meta:
        model = TbDimportaciones
        fields = '__all__'


class TbDimportacionesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbDimportaciones
        fields = '__all__'


class TbDimportacionRegistroSerializer(serializers.ModelSerializer):
    id_importacion = TbDimportacionesSerializer(read_only=True)

    class Meta:
        model = TbDimportacionRegistro
        fields = '__all__'


class TbDimportacionRegistroCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbDimportacionRegistro
        fields = '__all__'


class TbDpersonaReglaSerializer(serializers.ModelSerializer):
    id_persona = TbDpersonaSerializer(read_only=True)

    class Meta:
        model = TbDpersonaRegla
        fields = '__all__'


class TbDpersonaReglaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbDpersonaRegla
        fields = '__all__'


class TbDreglaCobroSerializer(serializers.ModelSerializer):
    id_usuario_registro = TbUserSerializer(read_only=True)
    id_tipo_regla = TbTipoReglaSerializer(read_only=True)

    class Meta:
        model = TbDreglaCobro
        fields = '__all__'


class TbDreglaCobroCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbDreglaCobro
        fields = '__all__'


class TbNtipoCobroSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNtipoCobro
        fields = '__all__'


class TbRfechaExcluidaSerializer(serializers.ModelSerializer):
    id_categoria_residente = TbNcategoriaResidenteSerializer(read_only=True)
    id_categoria = TbNcategoriaSerializer(read_only=True)
    id_evento = TbNeventoSerializer(read_only=True)

    class Meta:
        model = TbRfechaExcluida
        fields = '__all__'


class TbRfechaExcluidaCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbRfechaExcluida
        fields = '__all__'


class TbRimportacionReservacionSerializer(serializers.ModelSerializer):
    id_importacion = TbDimportacionSerializer(read_only=True)

    class Meta:
        model = TbRimportacionReservacion
        fields = '__all__'


class TbRimportacionReservacionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbRimportacionReservacion
        fields = '__all__'


class TbRpersonaExcluidaCobroSerializer(serializers.ModelSerializer):
    id_persona = TbDpersonaSerializer(read_only=True)
    id_importacion = TbDimportacionSerializer(read_only=True)
    id_usuario_registro = TbUserSerializer(read_only=True)

    class Meta:
        model = TbRpersonaExcluidaCobro
        fields = '__all__'


class TbRpersonaExcluidaCobroCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbRpersonaExcluidaCobro
        fields = '__all__'
