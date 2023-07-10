from rest_framework import viewsets, response, status
from .models import *
from .serializers import *


class TbDelementosMostrarViewSet(viewsets.ModelViewSet):
    queryset = TbDelementosMostrar.objects.all()
    serializer_class = TbDelementosMostrarSerializer


class TbDperiodoReservacionViewSet(viewsets.ModelViewSet):
    queryset = TbDperiodoReservacion.objects.all()
    serializer_class = TbDperiodoReservacion


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


class TbHistorialReservacionViewSet(viewsets.ModelViewSet):
    queryset = TbHistorialReservacion.objects.all()
    serializer_class = TbHistorialReservacionSerializer
