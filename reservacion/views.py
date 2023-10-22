from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from django_filters import rest_framework as filters

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
        user_institution = self.request.user.institucion
        return TbDperiodoReservacion.objects.filter(id_institucion=user_institution)

@extend_schema_view(
    create=extend_schema(tags=["Asocia personas a areas de reservacion"],
                         description="Asocia personas a areas de reservacion"),
    retrieve=extend_schema(
        tags=["Asocia personas a areas de reservacion"], description="Devuelve los detalles de un asociar personas a areas de reservacion"
    ),
    update=extend_schema(tags=["Asocia personas a areas de reservacion"],
                         description="Actualiza una asociacion de personas a areas de reservacion"),
    partial_update=extend_schema(
        tags=["Asocia personas a areas de reservacion"], description="Actualiza una asociacion de personas a areas de reservacion"
    ),
    destroy=extend_schema(tags=["Asocia personas a areas de reservacion"],
                          description="Destruye una asociacion de personas a areas de reservacion"),
    list=extend_schema(
        tags=["Asocia personas a areas de reservacion"],
        description="Lista las Asociaciones de personas a areas de reservaciones",
        parameters=[OpenApiParameter(name="query", required=False, type=str)],
    ),
)
class TbDresponsableAreaPersonasViewSet(viewsets.ModelViewSet):
    queryset = TbDresponsableAreaPersonas.objects.none()
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['id_estructura']

    def get_queryset(self):
        user_institucion = self.request.user.institucion
        return TbDresponsableAreaPersonas.objects.filter(id_institucion=user_institucion)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TbDresponsableAreaPersonasSerializer
        return TbDresponsableAreaPersonasCreateSerializer

@extend_schema_view(
    create=extend_schema(tags=["Asignar responsable de reservacion"],
                         description="Crea un responsable de reservacion"),
    retrieve=extend_schema(
        tags=["Asignar responsable de reservacion"], description="Devuelve los detalles de un responsable de reservacion"
    ),
    update=extend_schema(tags=["Asignar responsable de reservacion"],
                         description="Actualiza un responsable de reservacion"),
    partial_update=extend_schema(
        tags=["Asignar responsable de reservacion"], description="Actualiza un responsable de reservacion"
    ),
    destroy=extend_schema(tags=["Asignar responsable de reservacion"],
                          description="Destruye un responsable de reservacion"),
    list=extend_schema(
        tags=["Asignar responsable de reservacion"],
        description="Lista los responsables de reservaciones",
        parameters=[OpenApiParameter(name="query", required=False, type=str)],
    ),
)
class TbDresponsableReservacionViewSet(viewsets.ModelViewSet):
    queryset = TbDresponsableReservacion.objects.none()
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['id_estructura']
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TbDresponsableReservacionSerializer
        return TbDresponsableReservacionCreateSerializer

    def get_queryset(self):
        user_institucion = self.request.user.institucion
        return TbDresponsableReservacion.objects.filter(id_institucion=user_institucion)
