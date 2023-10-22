from .models import *
from .serializers import *
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from rest_framework import viewsets, permissions
from django_filters import rest_framework as filters

@extend_schema_view(
    create=extend_schema(tags=["Configuracion del proceso de reservacion"],
                         description="Crea un Configuracion del proceso de reservacion"),
    retrieve=extend_schema(
        tags=["Configuracion del proceso de reservacion"], description="Devuelve los detalles de un Configuracion del proceso de reservacion"
    ),
    update=extend_schema(tags=["Configuracion del proceso de reservacion"],
                         description="Actualiza un Configuracion del proceso de reservacion"),
    partial_update=extend_schema(
        tags=["Configuracion del proceso de reservacion"], description="Actualiza un Configuracion del proceso de reservacion"
    ),
    destroy=extend_schema(tags=["Configuracion del proceso de reservacion"],
                          description="Destruye un Configuracion del proceso de reservacion"),
    list=extend_schema(
        tags=["Configuracion del proceso de reservacion"],
        description="Lista los Configuracion del proceso de reservacion",
        parameters=[OpenApiParameter(name="query", required=False, type=str)],
    ),
)
class TbDconfiguracionProcesoViewSet(viewsets.ModelViewSet):
    queryset = TbDconfiguracionProceso.objects.none()
    serializer_class = TbDconfiguracionProcesoSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):

            user_institution = self.request.user.institucion
            return TbDconfiguracionProceso.objects.filter(id_institucion=user_institution)


@extend_schema_view(
    create=extend_schema(tags=["Datos de contactos"],
                         description="Crea un Datos de contactos"),
    retrieve=extend_schema(
        tags=["Datos de contactos"], description="Devuelve los detalles de un Datos de contacto"
    ),
    update=extend_schema(tags=["Datos de contactos"],
                         description="Actualiza un Datos de contacto"),
    partial_update=extend_schema(
        tags=["Datos de contactos"], description="Actualiza un Datos de contacto"
    ),
    destroy=extend_schema(tags=["Datos de contactos"],
                          description="Destruye un Datos de contacto"),
    list=extend_schema(
        tags=["Datos de contactos"],
        description="Lista los Datos de contactos",
        parameters=[OpenApiParameter(name="query", required=False, type=str)],
    ),
)
class TbDdatosContactoViewSet(viewsets.ModelViewSet):
    queryset = TbDdatosContacto.objects.none()
    serializer_class = TbDdatosContactoSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        user_institution = self.request.user.institucion
        return TbDdatosContacto.objects.filter(id_institucion=user_institution)


@extend_schema_view(
    create=extend_schema(tags=["Configuracion de comensales"],
                         description="Crea un Configuracion de comensales"),
    retrieve=extend_schema(
        tags=["Configuracion de comensales"], description="Devuelve los detalles de un Configuracion de comensale"
    ),
    update=extend_schema(tags=["Configuracion de comensales"],
                         description="Actualiza un Configuracion de comensale"),
    partial_update=extend_schema(
        tags=["Configuracion de comensales"], description="Actualiza un Configuracion de comensale"
    ),
    destroy=extend_schema(tags=["Configuracion de comensales"],
                          description="Destruye un Configuracion de comensale"),
    list=extend_schema(
        tags=["Configuracion de comensales"],
        description="Lista los Configuracion de comensales",
        parameters=[OpenApiParameter(name="query", required=False, type=str)],
    ),
)
class TbDconfiguracionPersonaViewSet(viewsets.ModelViewSet):
    queryset = TbDconfiguracionPersona.objects.none()
    serializer_class = TbDconfiguracionPersonaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):

        user_institution = self.request.user.institucion
        return TbDconfiguracionPersona.objects.filter(id_institucion=user_institution)


@extend_schema_view(
    create=extend_schema(tags=["Configuracion de comensales"],
                         description="Crea los valores de Configuracion de comensales"),
    retrieve=extend_schema(
        tags=["Configuracion de comensales"], description="Devuelve los detalles de los valores de Configuracion de comensale"
    ),
    update=extend_schema(tags=["Configuracion de comensales"],
                         description="Actualiza los valores de Configuracion de comensale"),
    partial_update=extend_schema(
        tags=["Configuracion de comensales"], description="Actualiza los valores de Configuracion de comensale"
    ),
    destroy=extend_schema(tags=["Configuracion de comensales"],
                          description="Destruye los valores de Configuracion de comensale"),
    list=extend_schema(
        tags=["Configuracion de comensales"],
        description="Lista los valores de Configuracion de comensales",
        parameters=[OpenApiParameter(name="query", required=False, type=str)],
    ),
)
class TbDvaloresConfiguracionPersonaViewSet(viewsets.ModelViewSet):
    queryset = TbDvaloresConfiguracionPersona.objects.none()
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['id_configuracion_persona']
    def get_queryset(self):

        user_institution = self.request.user.institucion
        return TbDvaloresConfiguracionPersona.objects.filter(id_institucion=user_institution)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TbDvaloresConfiguracionPersonaSerializer
        return TbDvaloresConfiguracionPersonaCreateSerializer

