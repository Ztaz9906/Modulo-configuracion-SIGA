from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *

@extend_schema_view(
    create=extend_schema(tags=["Elementos a mostrar"],
                         description="Crea un Elementos a mostrar"),
    retrieve=extend_schema(
        tags=["Elementos a mostrar"], description="Devuelve los detalles de un Elemento a mostrar"
    ),
    update=extend_schema(tags=["Elementos a mostrar"],
                         description="Actualiza un Elemento a mostrar"),
    partial_update=extend_schema(
        tags=["Elementos a mostrar"], description="Actualiza un Elemento a mostrar"
    ),
    destroy=extend_schema(tags=["Elementos a mostrar"],
                          description="Destruye un Elemento a mostrar"),
    list=extend_schema(
        tags=["Elementos a mostrar"],
        description="Lista los Elementos a mostrarse",
        parameters=[OpenApiParameter(name="query", required=False, type=str)],
    ),
)
class TbDelementosMostrarViewSet(viewsets.ModelViewSet):
    queryset = TbDelementosMostrar.objects.none()
    serializer_class = TbDelementosMostrarSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        if self.request.user.is_staff:
            return TbDelementosMostrar.objects.all()
        user_institution = self.request.user.institucion
        return TbDelementosMostrar.objects.filter(id_institucion=user_institution)
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
