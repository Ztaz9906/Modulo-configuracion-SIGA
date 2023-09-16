from rest_framework import serializers
from .models import *
from .serializerPost import *
from adminschema.serializer import TbUserSerializer, TbInstitucionSerializer
from base.serializers import TbDpersonaSerializer


######################################################################## Pertenece a distibucion ################################
class TbCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TbCategory
        fields = '__all__'


class TbNclasificacionEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNclasificacionEvento
        fields = '__all__'


class TbNhorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNhorario
        fields = '__all__'


class TbNeventoSerializer(serializers.ModelSerializer):
    id_horario = TbNhorarioSerializer(read_only=True)

    class Meta:
        model = TbNhorario
        fields = '__all__'


class RecursiveField(serializers.BaseSerializer):
    def to_representation(self, value):
        serializer = TbStructureSerializer(value, context=self.context)
        return serializer.data


class TbStructureSerializer(serializers.ModelSerializer):
    id_sub_director = TbDpersonaSerializer(read_only=True)
    id_tecnico_general = TbDpersonaSerializer(read_only=True)
    id_especialista_complejo = TbDpersonaSerializer(read_only=True)
    id_tecnico_atm = TbDpersonaSerializer(read_only=True)
    category = TbCategorySerializer(read_only=True)
    estructura_parent = RecursiveField(allow_null=True, read_only=True)

    class Meta:
        model = TbStructure
        fields = '__all__'

######################################################################## Final ############################################

######################################################################## Abastecimiento con asset ###################################################


class TbNtipoProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbNtipoProducto
        fields = '__all__'


class TbNunidadMedidaSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbNunidadMedida
        fields = '__all__'

####### Empieza esquema asset ##########


class TbDproductoSerializer(serializers.ModelSerializer):
    id_unidad_medida = TbNunidadMedidaSerializer(read_only=True)
    id_tipo_producto = TbNtipoProductoSerializer(read_only=True)

    class Meta:
        model = TbDproducto
        fields = '__all__'


######### Termina esquema assets #########
class TbDconfiguracionProductoSerializer(serializers.ModelSerializer):
    id_usuario_registro = TbUserSerializer(read_only=True)
    id_unidad_medida = TbNunidadMedidaSerializer(read_only=True)
    id_unidad_medida_merma = TbNunidadMedidaSerializer(read_only=True)
    id_unidad_medida_por_cada = TbNunidadMedidaSerializer(read_only=True)

    class Meta:
        model = TbDconfiguracionProducto
        fields = '__all__'

######################################################################## Final #################################################


class TbDaccesoEventoSecundarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbDaccesoEventoSecundario
        fields = '__all__'


class TbDpersonaPuertaSerializer(serializers.ModelSerializer):
    id_persona = TbDpersonaSerializer(read_only=True)
    id_usuario_registro = TbUserSerializer(read_only=True)
    id_usuario_modificacion = TbUserSerializer(read_only=True)
    id_puerta = TbStructureSerializer(read_only=True)

    class Meta:
        model = TbDpersonaIPPuerta
        fields = '__all__'


class TbDsolapinPerdidoSerializer(serializers.ModelSerializer):
    id_persona = TbDpersonaSerializer(read_only=True)
    id_usuario_registro = TbUserSerializer(read_only=True)

    class Meta:
        model = TbDsolapinPerdido
        fields = '__all__'


class TbNestadoTarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNestadoTarjeta
        fields = '__all__'


class TbNtipoTarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNtipoTarjeta
        fields = '__all__'


class TbDtarjetaAlimentacionSerializer(serializers.ModelSerializer):

    id_estado_tarjeta = TbNestadoTarjetaSerializer(read_only=True)
    id_usuario_registro = TbUserSerializer(read_only=True)
    id_tipo_tarjeta = TbNtipoTarjetaSerializer(read_only=True)
    id_usuario_modificacion = TbUserSerializer(read_only=True)

    class Meta:
        model = TbDtarjetaAlimentacion
        fields = '__all__'

################################################################ Distribucion #################################################################


class TbNclasificacionDistribucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNclasificacionDistribucion
        fields = '__all__'


class TbDdistribucionSerializer(serializers.ModelSerializer):
    id_usuario_registro = TbUserSerializer(read_only=True)
    id_clasificacion_distribucion = TbNclasificacionDistribucionSerializer(
        read_only=True)
    id_evento = TbNeventoSerializer(read_only=True)

    class Meta:
        model = TbDdistribucion
        fields = '__all__'


class TbDpersonaDistribucionSerializer(serializers.ModelSerializer):

    id_persona = models.ForeignKey(
        TbDpersona, models.DO_NOTHING, db_column='id_persona', blank=True, null=True)
    id_usuario_registro = TbUserSerializer(read_only=True)
    id_usuario_modificacion = TbUserSerializer(read_only=True)
    id_distribucion = TbDdistribucionSerializer(read_only=True)
    id_complejo_comedor = TbStructureSerializer(read_only=True)
    id_comedor = TbStructureSerializer(read_only=True)
    id_puerta = TbStructureSerializer(read_only=True)
    id_evento = TbNeventoSerializer(read_only=True)

    class Meta:
        model = TbDpersonaDistribucion
        fields = '__all__'


class TbDtarjetaDistribucionSerializer(serializers.ModelSerializer):

    id_usuario_registro = TbUserSerializer(read_only=True)
    id_usuario_modificacion = TbUserSerializer(read_only=True)
    id_distribucion = TbDdistribucionSerializer(read_only=True)
    id_complejo_comedor = TbStructureSerializer(read_only=True)
    id_comedor = TbStructureSerializer(read_only=True)
    id_puerta = TbStructureSerializer(read_only=True)
    id_evento = TbNeventoSerializer(read_only=True)
    id_tarjeta = TbDtarjetaAlimentacionSerializer(read_only=True)

    class Meta:
        model = TbDtarjetaDistribucion
        fields = '__all__'


class TbNreglaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNregla
        fields = '__all__'


class TbDvaloresReglaSerializer(serializers.ModelSerializer):
    id_regla = TbNreglaSerializer(read_only=True)
    # id_valor_regla = # hay q  ver para q es este id y por que esta ahi sin relacion alguna

    class Meta:
        model = TbDvaloresRegla
        fields = '__all__'

# Revisar por q este modelo en la base de datos no tiene ninguna relacion con las tablas


class TbLastDistribucionSerializer(serializers.ModelSerializer):
    # id_temp = models.AutoField(primary_key=True)
    # id_persona = models.CharField(max_length=255, blank=True, null=True)
    id_usuario_registro = models.IntegerField(blank=True, null=True)
    # fecha_registro = models.DateField(blank=True, null=True)
    # fecha_modificacion = models.DateField(blank=True, null=True)
    # id_usuario_modificacion = models.IntegerField(blank=True, null=True)
    # id_distribucion = models.IntegerField(blank=True, null=True)
    # id_complejo_comedor = models.IntegerField(blank=True, null=True)
    # id_comedor = models.IntegerField(blank=True, null=True)
    # id_puerta = models.IntegerField(blank=True, null=True)
    # id_evento = models.IntegerField(blank=True, null=True)

    class Meta:
        model = TbLastDistribucion
        fields = '__all__'


class TbNdiaSemanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNdiaSemana
        fields = '__all__'


class TbNrangoEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNrangoEvento
        fields = '__all__'


class TbRdistribucionReglaSerializer(serializers.ModelSerializer):
    id_distribucion = TbDdistribucionSerializer(read_only=True)

    class Meta:
        model = TbRdistribucionRegla
        fields = '__all__'


class TbRestructuraReglaSerializer(serializers.ModelSerializer):
    id_estructura = TbStructureSerializer(read_only=True)
    id_regla = TbNreglaSerializer(read_only=True)
    # id_valor_regla = # por que esta este id asi sin relacion aqui ojo

    class Meta:
        model = TbRestructuraRegla
        fields = '__all__'


class TbReventoHorarioSerializer(serializers.ModelSerializer):
    id_evento = TbNeventoSerializer(read_only=True)
    id_horario = TbNhorarioSerializer(read_only=True)

    class Meta:
        model = TbReventoHorario
        fields = '__all__'


class TbReventoRangoEventoSerializer(serializers.ModelSerializer):
    id_evento = TbNeventoSerializer(read_only=True)
    id_rango_evento = TbNrangoEventoSerializer(read_only=True)
    id_usuario_registro = TbUserSerializer(read_only=True)

    class Meta:
        model = TbReventoRangoEvento
        fields = '__all__'


class TbRhorarioDiaSemanaSerializer(serializers.ModelSerializer):
    id_horario = TbNhorarioSerializer(read_only=True)
    id_dia_semana = TbNdiaSemanaSerializer(read_only=True)

    class Meta:
        model = TbRhorarioDiaSemana
        fields = '__all__'

# revisar por que esta sin ralacion alguna ninnguno de estos id


################################################################    Fin      #################################################################

################################################################ Esquema cajero ##############################################################


class TbDconfiguracionTarjetaSerializer(serializers.ModelSerializer):
    id_tarjeta_alimentacion = TbDtarjetaAlimentacionSerializer(read_only=True)
    id_complejo_comedor = TbStructureSerializer(read_only=True)
    id_comedor = TbStructureSerializer(read_only=True)
    id_puerta = TbStructureSerializer(read_only=True)
    id_evento = TbNeventoSerializer(read_only=True)

    class Meta:
        model = TbDconfiguracionTarjeta
        fields = '__all__'


class TbNestadoMovimientoAsignacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNestadoMovimientoAsignacion
        fields = '__all__'


class TbMovimientoAsignacionSerializer(serializers.ModelSerializer):
    id_puerta_origen = TbStructureSerializer(read_only=True)
    id_puerta_destino = TbStructureSerializer(read_only=True)
    id_evento = TbNeventoSerializer(read_only=True)
    id_usuario_registro = TbUserSerializer(read_only=True)
    id_estado_movimiento_asignacion = TbNestadoMovimientoAsignacionSerializer(
        read_only=True)
    id_usuario_modificacion = TbUserSerializer(read_only=True)

    class Meta:
        model = TbMovimientoAsignacion
        fields = '__all__'


class TbRpersonaTarjetaSerializer(serializers.ModelSerializer):
    id_persona = TbDpersonaSerializer(read_only=True)
    id_tarjeta = TbDtarjetaAlimentacionSerializer(read_only=True)

    class Meta:
        model = TbRpersonaTarjeta
        fields = '__all__'
########################################################################## Fin ###############################################################################
