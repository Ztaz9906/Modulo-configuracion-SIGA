from rest_framework import serializers
from .models import *

######################################################################## Pertenece a distibucion ################################


class TbCategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbCategory
        fields = '__all__'


class TbNclasificacionEventoCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbNclasificacionEvento
        fields = '__all__'


class TbNhorarioCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbNhorario
        fields = '__all__'


class TbNeventoCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbNevento
        fields = '__all__'


class TbStructureCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbStructure
        fields = '__all__'
######################################################################## Final ############################################

######################################################################## Abastecimiento con asset ###################################################


class TbNtipoProductoCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbNtipoProducto
        fields = '__all__'


class TbNclasificacionPlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNclasificacionPlato
        fields = '__all__'


class TbNunidadMedidaCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbNunidadMedida
        fields = '__all__'

####### Empieza esquema asset ##########


class TbDproductoCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbDproducto
        fields = '__all__'

######### Termina esquema assets #########


class TbDconfiguracionProductoCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbDconfiguracionProducto
        fields = '__all__'

######################################################################## Final #################################################


class TbDaccesoEventoSecundarioCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbDaccesoEventoSecundario
        fields = '__all__'


class TbDpersonaPuertaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbDpersonaIPPuerta
        fields = '__all__'


class TbDsolapinPerdidoCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbDsolapinPerdido
        fields = '__all__'


class TbNestadoTarjetaCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbNestadoTarjeta
        fields = '__all__'


class TbNtipoTarjetaCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbNtipoTarjeta
        fields = '__all__'


class TbDtarjetaAlimentacionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbDtarjetaAlimentacion
        fields = ['id_usuario_registro', 'id_tipo_tarjeta',
                  'id_institucion', 'id_estado_tarjeta', 'fecha_inicio', 'fecha_fin']

################################################################ Distribucion #################################################################


class TbNclasificacionDistribucionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbNclasificacionDistribucion
        fields = '__all__'


class TbDdistribucionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbDdistribucion
        fields = '__all__'


class TbDpersonaDistribucionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbDpersonaDistribucion
        fields = '__all__'


class TbDtarjetaDistribucionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbDtarjetaDistribucion
        fields = '__all__'


class TbNreglaCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbNregla
        fields = '__all__'


class TbDvaloresReglaCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbNregla
        fields = '__all__'

# Revisar por q este modelo en la base de datos no tiene ninguna relacion con las tablas


class TbLastDistribucionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbLastDistribucion
        fields = '__all__'


class TbNrangoEventoCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbNrangoEvento
        fields = '__all__'


class TbRdistribucionReglaCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbRdistribucionRegla
        fields = '__all__'


class TbRestructuraReglaCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbRestructuraRegla
        fields = '__all__'


class TbReventoHorarioCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbReventoHorario
        fields = '__all__'


class TbReventoRangoEventoCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbReventoRangoEvento
        fields = '__all__'


################################################################    Fin      #################################################################
################################################################ Esquema cajero ##############################################################


class TbDconfiguracionTarjetaCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbDconfiguracionTarjeta
        fields = '__all__'


class TbNestadoMovimientoAsignacionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbNestadoMovimientoAsignacion
        fields = '__all__'


class TbMovimientoAsignacionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbMovimientoAsignacion
        fields = '__all__'


class TbRpersonaTarjetaCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbRpersonaTarjeta
        fields = '__all__'
########################################################################## Fin ###############################################################################
