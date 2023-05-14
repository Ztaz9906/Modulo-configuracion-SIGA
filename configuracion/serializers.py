from rest_framework import serializers
from .models import *
from adminschema.serializer import TbUserSerializer
from base.serializers import TbNcategoriaResidenteSerializer,TbNcategoriaSerializer,TbNestructuraSerializer,TbNtipoCursoSerializer
from cajero.serializerGet import TbStructureSerializer
from cajero.serializerGet import TbNeventoSerializer,TbNdiaSemanaSerializer


class TbDavisosSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbDavisos
        fields = '__all__'

class TbDconfiguracionCobroSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbDconfiguracionCobro
        fields = '__all__'

class TbDconfiguracionElasticSerializer(serializers.ModelSerializer):
    id_usuario_registro = TbUserSerializer(read_only=True)
    class Meta:
        model = TbDconfiguracionElastic
        fields = '__all__'
class TbDconfiguracionElasticCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbDconfiguracionElastic
        fields = '__all__'
   
class TbDconfiguracionEventoAccesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbDconfiguracionEventoAcceso
        fields = '__all__'

class TbDconfiguracionPersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbDconfiguracionPersona
        fields = '__all__'

class TbDconfiguracionProcesoSerializer(serializers.ModelSerializer):
    id_usuario_registro = TbUserSerializer(read_only=True)
    class Meta:
        model = TbDconfiguracionProceso
        fields = '__all__'

class TbDconfiguracionProcesoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbDconfiguracionProceso
        fields = '__all__'
    
    

class TbDconfiguracionRabbitmqSerializer(serializers.ModelSerializer):
    id_usuario_registro = TbUserSerializer(read_only=True)
    class Meta:
        model = TbDconfiguracionRabbitmq
        fields = '__all__'
    
class TbDconfiguracionRabbitmqCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbDconfiguracionRabbitmq
        fields = '__all__'

class TbDcronSerializer(serializers.ModelSerializer):
    id_usuario_registro = TbUserSerializer(read_only=True)
    class Meta:
        model = TbDcron
        fields = '__all__'

class TbDcronCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbDcron
        fields = '__all__'

class TbDdatosContactoSerializer(serializers.ModelSerializer):
    id_usuario_registro = TbUserSerializer(read_only=True)
    class Meta:
        model = TbDdatosContacto
        fields = '__all__'
class TbDdatosContactoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbDdatosContacto
        fields = '__all__'   


class TbDplanificacionMenuSerializer(serializers.ModelSerializer):
    id_complejo = TbStructureSerializer(read_only=True)
    class Meta:
        model = TbDplanificacionMenu
        fields = '__all__'

class TbDplanificacionMenuCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbDplanificacionMenu
        fields = '__all__'

class TbDvaloresConfiguracionCobroSerializer(serializers.ModelSerializer):
    id_valores_configuracion_cobro = models.AutoField(primary_key=True)
    id_configuracion_cobro = TbDconfiguracionCobroSerializer(read_only=True)
    id_categoria = TbNcategoriaSerializer(read_only=True)
    id_categoria_residente = TbNcategoriaResidenteSerializer(read_only=True)
    id_estructura = TbNestructuraSerializer(read_only=True)
    id_tipo_curso = TbNtipoCursoSerializer(read_only=True)
    id_evento = TbNeventoSerializer(read_only=True)
    class Meta:
        model = TbDvaloresConfiguracionCobro
        fields = '__all__'

class TbDvaloresConfiguracionCobroCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbDvaloresConfiguracionCobro
        fields = '__all__'  


class TbDvaloresConfiguracionEventoAccesoSerializer(serializers.ModelSerializer):
    id_categoria = TbNcategoriaSerializer(read_only=True)
    id_estructura = TbNestructuraSerializer(read_only=True)
    id_tipo_curso = TbNtipoCursoSerializer(read_only=True)
    id_evento = TbNeventoSerializer(read_only=True)
    id_categoria_residente = TbNcategoriaResidenteSerializer(read_only=True)
    id_configuracion_evento_acceso = TbDconfiguracionEventoAccesoSerializer(read_only=True)
    id_dia_semana = TbNdiaSemanaSerializer(read_only=True)
    class Meta:
        model = TbDvaloresConfiguracionEventoAcceso
        fields = '__all__'
    
class TbDvaloresConfiguracionEventoAccesoCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TbDvaloresConfiguracionEventoAcceso
        fields = '__all__'
       

    


class TbDvaloresConfiguracionPersonaSerializer(serializers.ModelSerializer):
    id_configuracion_persona = TbDconfiguracionPersonaSerializer(read_only=True)
    id_categoria = TbNcategoriaSerializer(read_only=True)
    id_categoria_residente = TbNcategoriaResidenteSerializer
    id_estructura = TbNestructuraSerializer(read_only=True)
    id_tipo_curso = TbNtipoCursoSerializer(read_only=True)
    class Meta:
        model = TbDvaloresConfiguracionPersona
        fields = '__all__'
    
class TbDvaloresConfiguracionPersonaCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbDvaloresConfiguracionPersona
        fields = '__all__'   
