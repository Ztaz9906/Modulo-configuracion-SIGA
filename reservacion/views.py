from django_filters import rest_framework as filters
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *


class TbDelementosMostrarViewSet(viewsets.ModelViewSet):
    queryset = TbDelementosMostrar.objects.all()
    serializer_class = TbDelementosMostrarSerializer

@extend_schema_view(
    create=extend_schema(tags=["Periodo de Reservacion"],
                         description="Crea un Periodo de Reservacion"),
    retrieve=extend_schema(
        tags=["Periodo de Reservacion"], description="Devuelve los detalles de un Periodo de Reservacion"
    ),
    update=extend_schema(tags=["Periodo de Reservacion"],
                         description="Actualiza un Periodo de Reservacion"),
    partial_update=extend_schema(
        tags=["Periodo de Reservacion"], description="Actualiza un Periodo de Reservacion"
    ),
    destroy=extend_schema(tags=["Periodo de Reservacion"],
                          description="Destruye un Periodo de Reservacion"),
    list=extend_schema(
        tags=["Periodo de Reservacion"],
        description="Lista los Periodo de Reservaciones",
        parameters=[OpenApiParameter(name="query", required=False, type=str)],
    ),
)
class TbDperiodoReservacionViewSet(viewsets.ModelViewSet):
    queryset = TbDperiodoReservacion.objects.none()
    serializer_class = TbDperiodoReservacionSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        if self.request.user.is_staff:
            return TbDperiodoReservacion.objects.all()
        user_institution = self.request.user.institucion
        return TbDperiodoReservacion.objects.filter(id_institucion=user_institution)
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
