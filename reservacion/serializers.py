from rest_framework import serializers
from .models import *
from adminschema.serializer import TbUserSerializer
from base.serializers import TbDpersonaSerializer,TbNestructuraSerializer
from cajero.serializerGet import TbNeventoSerializer,TbDpersonaDistribucionSerializer
from configuracion.serializers import TbDconfiguracionCobroSerializer
from cajero.serializerGet import TbNplatoSerializer,TbDmenuSerializer

class TbDelementosMostrarSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbDelementosMostrar
        fields = '__all__'


class TbDperiodoReservacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbDperiodoReservacion
        fields = '__all__'
    
class TbDreservacionSerializer(serializers.ModelSerializer):
    id_reservacion = models.AutoField(primary_key=True)
    id_persona = TbDpersonaSerializer(read_only=True)
    id_evento = TbNeventoSerializer(read_only=True)
    id_configuracion_cobro = TbDconfiguracionCobroSerializer(read_only=True)
    id_persona_distribucion = TbDpersonaDistribucionSerializer(read_only=True)
    class Meta:
        model = TbDreservacion
        fields = '__all__'

class TbDreservacionCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TbDreservacion
        fields = '__all__'   

class TbDresponsableAreaPersonasSerializer(serializers.ModelSerializer):
    id_persona = TbDpersonaSerializer(read_only=True)
    id_estructura = TbNestructuraSerializer(read_only=True)
    id_persona_registro = TbUserSerializer(read_only=True)
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
    id_persona_registro = TbUserSerializer(read_only=True)
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


class TbRreservacionPlatoSerializer(serializers.ModelSerializer):
    id_reservacion = TbDreservacionSerializer(read_only=True)
    id_plato = TbNplatoSerializer(read_only=True)
    id_menu = TbDmenuSerializer(read_only=True)
    id_evento = TbNeventoSerializer(read_only=True)
    id_persona = TbDpersonaSerializer(read_only=True)
    class Meta:
        model = TbRreservacionPlato
        fields = '__all__'
class TbRreservacionPlatoCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TbRreservacionPlato
        fields = '__all__'
    
    

class TbRticketReservacionSerializer(serializers.ModelSerializer):
    id_reservacion = TbDreservacionSerializer(read_only=True)
    id_usuario_registro = TbUserSerializer(read_only=True)
    class Meta:
        model = TbRticketReservacion
        fields = '__all__'

class TbRticketReservacionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbRticketReservacion
        fields = '__all__'  