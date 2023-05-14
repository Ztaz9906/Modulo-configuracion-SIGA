from rest_framework import viewsets,response, status
from .models import *
from .serializers import *

class TbDavisosViewSet(viewsets.ModelViewSet):
    queryset = TbDavisos.objects.all()
    serializer_class = TbDavisosSerializer

class TbDconfiguracionCobroViewSet(viewsets.ModelViewSet):
    queryset = TbDconfiguracionCobro.objects.all()
    serializer_class = TbDconfiguracionCobroSerializer

class TbDconfiguracionElasticViewSet(viewsets.ModelViewSet):
    queryset = TbDconfiguracionElastic.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDconfiguracionElasticCreateSerializer
        else:
            return TbDconfiguracionElasticSerializer

class TbDconfiguracionEventoAccesoViewSet(viewsets.ModelViewSet):
    queryset = TbDconfiguracionEventoAcceso.objects.all()
    serializer_class = TbDconfiguracionEventoAccesoSerializer
    
class TbDconfiguracionPersonaViewSet(viewsets.ModelViewSet):
    queryset = TbDconfiguracionPersona.objects.all()
    serializer_class = TbDconfiguracionPersonaSerializer
    
class TbDconfiguracionProcesoViewSet(viewsets.ModelViewSet):
    queryset = TbDconfiguracionProceso.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDconfiguracionProcesoCreateSerializer
        else:
            return TbDconfiguracionProcesoSerializer

class TbDconfiguracionRabbitmqViewSet(viewsets.ModelViewSet):
    queryset = TbDconfiguracionRabbitmq.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDconfiguracionRabbitmqCreateSerializer
        else:
            return TbDconfiguracionRabbitmqSerializer

class TbDcronViewSet(viewsets.ModelViewSet):
    queryset = TbDcron.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDcronCreateSerializer
        else:
            return TbDcronSerializer

class TbDdatosContactoViewSet(viewsets.ModelViewSet):
    queryset = TbDdatosContacto.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDdatosContactoCreateSerializer
        else:
            return TbDdatosContactoSerializer

class TbDplanificacionMenuViewSet(viewsets.ModelViewSet):
    queryset = TbDplanificacionMenu.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDplanificacionMenuCreateSerializer
        else:
            return TbDplanificacionMenuSerializer

class TbDvaloresConfiguracionCobroViewSet(viewsets.ModelViewSet):
    queryset = TbDvaloresConfiguracionCobro.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDvaloresConfiguracionCobroCreateSerializer
        else:
            return TbDvaloresConfiguracionCobroSerializer

class TbDvaloresConfiguracionEventoAccesoViewSet(viewsets.ModelViewSet):
    queryset = TbDvaloresConfiguracionEventoAcceso.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDvaloresConfiguracionEventoAccesoCreateSerializer
        else:
            return TbDvaloresConfiguracionEventoAccesoSerializer

class TbDvaloresConfiguracionPersonaViewSet(viewsets.ModelViewSet):
    queryset = TbDvaloresConfiguracionPersona.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDvaloresConfiguracionPersonaCreateSerializer
        else:
            return TbDvaloresConfiguracionPersonaSerializer
    
