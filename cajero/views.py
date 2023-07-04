from rest_framework import viewsets
from .models import *
from .serializerGet import *
from .serializerPost import *


######################################################################## Pertenece a distibucion ################################
class TbCategoryViewSet(viewsets.ModelViewSet):
    queryset = TbCategory.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbCategoryCreateSerializer
        else:
            return TbCategorySerializer


class TbNclasificacionEventoViewSet(viewsets.ModelViewSet):
    queryset = TbNclasificacionEvento.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbNclasificacionEventoCreateSerializer
        else:
            return TbNclasificacionEventoSerializer


class TbNhorarioViewSet(viewsets.ModelViewSet):
    queryset = TbNhorario.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbNhorarioCreateSerializer
        else:
            return TbNhorarioSerializer


class TbNeventoViewSet(viewsets.ModelViewSet):
    queryset = TbNevento.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbNeventoCreateSerializer
        else:
            return TbNeventoSerializer


class TbStructureViewSet(viewsets.ModelViewSet):
    queryset = TbStructure.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbStructureCreateSerializer
        else:
            return TbStructureSerializer
######################################################################## Final ############################################

######################################################################## Abastecimiento con asset ###################################################


class TbNtipoProductoViewSet(viewsets.ModelViewSet):
    queryset = TbNtipoProducto.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbNtipoProductoCreateSerializer
        else:
            return TbNtipoProductoSerializer


class TbNunidadMedidaViewSet(viewsets.ModelViewSet):
    queryset = TbNunidadMedida.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbNunidadMedidaCreateSerializer
        else:
            return TbNunidadMedidaSerializer

####### Empieza esquema asset ##########


class TbDproductoViewSet(viewsets.ModelViewSet):
    queryset = TbDproducto.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDproductoCreateSerializer
        else:
            return TbDproductoSerializer


######### Termina esquema assets #########
class TbDconfiguracionProductoViewSet(viewsets.ModelViewSet):
    queryset = TbDconfiguracionProducto.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDconfiguracionProductoCreateSerializer
        else:
            return TbDconfiguracionProductoSerializer

######################################################################## Final #################################################


class TbDaccesoEventoSecundarioViewSet(viewsets.ModelViewSet):
    queryset = TbDaccesoEventoSecundario.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDaccesoEventoSecundarioCreateSerializer
        else:
            return TbDaccesoEventoSecundarioSerializer


class TbDpersonaPuertaViewSet(viewsets.ModelViewSet):
    queryset = TbDpersonaIPPuerta.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDpersonaPuertaCreateSerializer
        else:
            return TbDpersonaPuertaSerializer


class TbDsolapinPerdidoViewSet(viewsets.ModelViewSet):
    queryset = TbDsolapinPerdido.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDsolapinPerdidoCreateSerializer
        else:
            return TbDsolapinPerdidoSerializer


class TbNestadoTarjetaViewSet(viewsets.ModelViewSet):
    queryset = TbNestadoTarjeta.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbNestadoTarjetaCreateSerializer
        else:
            return TbNestadoTarjetaSerializer


class TbNtipoTarjetaViewSet(viewsets.ModelViewSet):
    queryset = TbNtipoTarjeta.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbNtipoTarjetaCreateSerializer
        else:
            return TbNtipoTarjetaSerializer


class TbDtarjetaAlimentacionViewSet(viewsets.ModelViewSet):
    queryset = TbDtarjetaAlimentacion.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDtarjetaAlimentacionCreateSerializer
        else:
            return TbDtarjetaAlimentacionSerializer

################################################################ Distribucion #################################################################


class TbNclasificacionDistribucionViewSet(viewsets.ModelViewSet):
    queryset = TbNclasificacionDistribucion.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbNclasificacionDistribucionCreateSerializer
        else:
            return TbNclasificacionDistribucionSerializer


class TbDdistribucionViewSet(viewsets.ModelViewSet):
    queryset = TbDdistribucion.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDdistribucionCreateSerializer
        else:
            return TbDdistribucionSerializer


class TbDpersonaDistribucionViewSet(viewsets.ModelViewSet):
    queryset = TbDpersonaDistribucion.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDpersonaDistribucionCreateSerializer
        else:
            return TbDpersonaDistribucionSerializer


class TbDtarjetaDistribucionViewSet(viewsets.ModelViewSet):
    queryset = TbDtarjetaDistribucion.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDtarjetaDistribucionCreateSerializer
        else:
            return TbDtarjetaDistribucionSerializer


class TbNreglaViewSet(viewsets.ModelViewSet):
    queryset = TbNregla.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbNreglaCreateSerializer
        else:
            return TbNreglaSerializer


class TbDvaloresReglaViewSet(viewsets.ModelViewSet):
    queryset = TbDvaloresRegla.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDvaloresReglaCreateSerializer
        else:
            return TbDvaloresReglaSerializer

# Revisar por q este modelo en la base de datos no tiene ninguna relacion con las tablas


class TbLastDistribucionViewSet(viewsets.ModelViewSet):
    queryset = TbLastDistribucion.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbLastDistribucionCreateSerializer
        else:
            return TbLastDistribucionSerializer


class TbNdiaSemanaViewSet(viewsets.ModelViewSet):
    queryset = TbNdiaSemana.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbNdiaSemanaCreateSerializer
        else:
            return TbNdiaSemanaSerializer


class TbNrangoEventoViewSet(viewsets.ModelViewSet):
    queryset = TbNrangoEvento.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbNrangoEventoCreateSerializer
        else:
            return TbNrangoEventoSerializer


class TbRdistribucionReglaViewSet(viewsets.ModelViewSet):
    queryset = TbRdistribucionRegla.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbRdistribucionReglaCreateSerializer
        else:
            return TbRdistribucionReglaSerializer


class TbRestructuraReglaViewSet(viewsets.ModelViewSet):
    queryset = TbRestructuraRegla.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbRestructuraReglaCreateSerializer
        else:
            return TbRestructuraReglaSerializer


class TbReventoHorarioViewSet(viewsets.ModelViewSet):
    queryset = TbReventoHorario.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbReventoHorarioCreateSerializer
        else:
            return TbReventoHorarioSerializer


class TbReventoRangoEventoViewSet(viewsets.ModelViewSet):
    queryset = TbReventoRangoEvento.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbReventoRangoEventoCreateSerializer
        else:
            return TbReventoRangoEventoSerializer


class TbRhorarioDiaSemanaViewSet(viewsets.ModelViewSet):
    queryset = TbRhorarioDiaSemana.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbRhorarioDiaSemanaCreateSerializer
        else:
            return TbRhorarioDiaSemanaSerializer

# revisar por que esta sin ralacion alguna ninnguno de estos id


################################################################    Fin      #################################################################

################################################################ Esquema cajero ##############################################################


class TbDconfiguracionTarjetaViewSet(viewsets.ModelViewSet):
    queryset = TbDconfiguracionTarjeta.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDconfiguracionTarjetaCreateSerializer
        else:
            return TbDconfiguracionTarjetaSerializer


class TbNestadoMovimientoAsignacionViewSet(viewsets.ModelViewSet):
    queryset = TbNestadoMovimientoAsignacion.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbNestadoMovimientoAsignacionCreateSerializer
        else:
            return TbNestadoMovimientoAsignacionSerializer


class TbMovimientoAsignacionViewSet(viewsets.ModelViewSet):
    queryset = TbMovimientoAsignacion.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbMovimientoAsignacionCreateSerializer
        else:
            return TbMovimientoAsignacionSerializer


class TbRpersonaTarjetaViewSet(viewsets.ModelViewSet):
    queryset = TbRpersonaTarjeta.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbRpersonaTarjetaCreateSerializer
        else:
            return TbRpersonaTarjetaSerializer
########################################################################## Fin ###############################################################################
