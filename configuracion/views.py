from rest_framework import viewsets
from .models import *
from .serializers import *


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


class TbDdatosContactoViewSet(viewsets.ModelViewSet):
    queryset = TbDdatosContacto.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDdatosContactoCreateSerializer
        else:
            return TbDdatosContactoSerializer


class TbDvaloresConfiguracionPersonaViewSet(viewsets.ModelViewSet):
    queryset = TbDvaloresConfiguracionPersona.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDvaloresConfiguracionPersonaCreateSerializer
        else:
            return TbDvaloresConfiguracionPersonaSerializer
