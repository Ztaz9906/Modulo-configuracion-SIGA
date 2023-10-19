
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from rest_framework import viewsets, permissions
from django_filters import rest_framework as filters
from .models import *
from .serializers import *


@extend_schema_view(
    create=extend_schema(tags=["Tipo de cobro"],
                         description="Crea un Tipo de cobro"),
    retrieve=extend_schema(
        tags=["Tipo de cobro"], description="Devuelve los detalles de un Tipo de cobro"
    ),
    update=extend_schema(tags=["Tipo de cobro"],
                         description="Actualiza un Tipo de cobro"),
    partial_update=extend_schema(
        tags=["Tipo de cobro"], description="Actualiza un Configuracion del proceso de reservacion"
    ),
    destroy=extend_schema(tags=["Tipo de cobro"],
                          description="Destruye un Tipo de cobro"),
    list=extend_schema(
        tags=["Tipo de cobro"],
        description="Lista los Tipo de cobro",
        parameters=[OpenApiParameter(name="query", required=False, type=str)],
    ),
)
class TbNtipoCobroViewSet(viewsets.ModelViewSet):
    queryset = TbNtipoCobro.objects.none()
    serializer_class = TbNtipoCobroSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
            if self.request.user.is_staff:
                return TbNtipoCobro.objects.all()
            user_institution = self.request.user.institucion
            return TbNtipoCobro.objects.filter(id_institucion=user_institution)


@extend_schema_view(
    create=extend_schema(tags=["Configuracion de cobro"],
                         description="Crea un Configuracion de cobro"),
    retrieve=extend_schema(
        tags=["Configuracion de cobro"], description="Devuelve los detalles de un Configuracion de cobro"
    ),
    update=extend_schema(tags=["Configuracion de cobro"],
                         description="Actualiza un Configuracion de cobro"),
    partial_update=extend_schema(
        tags=["Configuracion de cobro"], description="Actualiza un Configuracion del proceso de reservacion"
    ),
    destroy=extend_schema(tags=["Configuracion de cobro"],
                          description="Destruye un Configuracion de cobro"),
    list=extend_schema(
        tags=["Configuracion de cobro"],
        description="Lista los Configuracion de cobro",
        parameters=[OpenApiParameter(name="query", required=False, type=str)],
    ),
)
class TbNconfiguracionCobroViewSet(viewsets.ModelViewSet):
    queryset = TbNconfiguracionCobro.objects.none()
    serializer_class = TbNconfiguracionCobroSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
            if self.request.user.is_staff:
                return TbNconfiguracionCobro.objects.all()
            user_institution = self.request.user.institucion
            return TbNconfiguracionCobro.objects.filter(id_institucion=user_institution)


@extend_schema_view(
    create=extend_schema(tags=["Valores de configuracion de cobro"],
                         description="Crea un Valores de configuracion de cobro"),
    retrieve=extend_schema(
        tags=["Valores de configuracion de cobro"], description="Devuelve los detalles de un Valores de configuracion de cobro"
    ),
    update=extend_schema(tags=["Valores de configuracion de cobro"],
                         description="Actualiza un Valores de configuracion de cobro"),
    partial_update=extend_schema(
        tags=["Valores de configuracion de cobro"], description="Actualiza un Configuracion del proceso de reservacion"
    ),
    destroy=extend_schema(tags=["Valores de configuracion de cobro"],
                          description="Destruye un Valores de configuracion de cobro"),
    list=extend_schema(
        tags=["Valores de configuracion de cobro"],
        description="Lista los Tipo de cobro",
        parameters=[OpenApiParameter(name="query", required=False, type=str)],
    ),
)
class TbNvaloresConfiguracionCobroViewSet(viewsets.ModelViewSet):
    queryset = TbNvaloresConfiguracionCobro.objects.none()
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['id_configuracion_cobro']

    def get_queryset(self):
            if self.request.user.is_staff:
                return TbNvaloresConfiguracionCobro.objects.all()
            user_institution = self.request.user.institucion
            return TbNvaloresConfiguracionCobro.objects.filter(id_institucion=user_institution)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TbNvaloresConfiguracionCobroSerializer
        return TbNvaloresConfiguracionCobroCreateSerializer