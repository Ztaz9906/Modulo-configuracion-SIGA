from rest_framework import viewsets,response, status
from .models import *
from .serializers import *

class TbDelementosMostrarViewSet(viewsets.ModelViewSet):
    queryset = TbDelementosMostrar.objects.all()
    serializer_class = TbDelementosMostrarSerializer

class TbDperiodoReservacionViewSet(viewsets.ModelViewSet):
    queryset = TbDperiodoReservacion.objects.all()
    serializer_class = TbDperiodoReservacion
    
class TbDreservacionViewSet(viewsets.ModelViewSet):
    queryset = TbDreservacion.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDreservacionCreateSerializer
        else:
            return TbDreservacionSerializer

class TbDresponsableAreaPersonasViewSet(viewsets.ModelViewSet):
    queryset = TbDresponsableAreaPersonas.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDresponsableAreaPersonasCreateSerializer
        else:
            return TbDresponsableAreaPersonasSerializer


class TbDresponsableReservacionViewSet(viewsets.ModelViewSet):
    queryset = TbDresponsableReservacion.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDresponsableReservacionCreateSerializer
        else:
            return TbDresponsableReservacionSerializer

# por que esta tabla no tiene relacion con ninguna en la base de datos revisar
class TbHistorialReservacionViewSet(viewsets.ModelViewSet):
    queryset = TbHistorialReservacion.objects.all()
    serializer_class = TbHistorialReservacionSerializer


class TbRreservacionPlatoViewSet(viewsets.ModelViewSet):
    queryset = TbRreservacionPlato.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbRreservacionPlatoCreateSerializer
        else:
            return TbRreservacionPlatoSerializer


class TbRticketReservacionViewSet(viewsets.ModelViewSet):
    queryset = TbRticketReservacion.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbRticketReservacionCreateSerializer
        else:
            return TbRticketReservacionSerializer
