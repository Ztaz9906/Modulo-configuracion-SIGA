from .models import *
from .serializers import *
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from rest_framework import viewsets, permissions

class TbDconfiguracionPersonaViewSet(viewsets.ModelViewSet):
    queryset = TbDconfiguracionPersona.objects.all()
    serializer_class = TbDconfiguracionPersonaSerializer

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
            if self.request.user.is_staff:
                return TbDconfiguracionProceso.objects.all()
            user_institution = self.request.user.institucion
            return TbDconfiguracionProceso.objects.filter(id_institucion=user_institution)
@extend_schema_view(
    create=extend_schema(tags=["Datos de contacto"],
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
        if self.request.user.is_staff:
            return TbDdatosContacto.objects.all()
        user_institution = self.request.user.institucion
        return TbDdatosContacto.objects.filter(id_institucion=user_institution)

class TbDvaloresConfiguracionPersonaViewSet(viewsets.ModelViewSet):
    queryset = TbDvaloresConfiguracionPersona.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDvaloresConfiguracionPersonaCreateSerializer
        else:
            return TbDvaloresConfiguracionPersonaSerializer
