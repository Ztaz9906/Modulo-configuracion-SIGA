
from rest_framework import viewsets,response, status
from .models import *
from .serializers import *

class TbTipoReglaViewSet(viewsets.ModelViewSet):
    queryset = TbTipoRegla.objects.all()
    serializer_class = TbTipoReglaSerializer

class TbNestadoImportacionViewSet(viewsets.ModelViewSet):
    queryset = TbNestadoImportacion.objects.all()
    serializer_class = TbNestadoImportacionSerializer

class TbDimportacionViewSet(viewsets.ModelViewSet):
    queryset = TbDimportacion.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDimportacionCreateSerializer
        else:
            return TbDimportacionSerializer

class TbDimportacionesViewSet(viewsets.ModelViewSet):
    queryset = TbDimportaciones.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDimportacionesCreateSerializer
        else:
            return TbDimportacionesSerializer

class TbDimportacionRegistroViewSet(viewsets.ModelViewSet):
    queryset = TbDimportacionRegistro.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDimportacionRegistroCreateSerializer
        else:
            return TbDimportacionRegistroSerializer

class TbDpersonaReglaViewSet(viewsets.ModelViewSet):
    queryset = TbDpersonaRegla.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDpersonaReglaCreateSerializer
        else:
            return TbDpersonaReglaSerializer

class TbDreglaCobroViewSet(viewsets.ModelViewSet):
    queryset = TbDreglaCobro.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDreglaCobroCreateSerializer
        else:
            return TbDreglaCobroSerializer

class TbNtipoCobroViewSet(viewsets.ModelViewSet):
    queryset = TbNtipoCobro.objects.all()
    serializer_class = TbNtipoCobroSerializer
    
class TbRfechaExcluidaViewSet(viewsets.ModelViewSet):
    queryset = TbRfechaExcluida.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbRfechaExcluidaCreateSerializer
        else:
            return TbRfechaExcluidaSerializer

class TbRimportacionReservacionViewSet(viewsets.ModelViewSet):
    queryset = TbRimportacionReservacion.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbRimportacionReservacionCreateSerializer
        else:
            return TbRimportacionReservacionSerializer

class TbRpersonaExcluidaCobroViewSet(viewsets.ModelViewSet):
    queryset = TbRpersonaExcluidaCobro.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbRpersonaExcluidaCobroCreateSerializer
        else:
            return TbRpersonaExcluidaCobroSerializer
