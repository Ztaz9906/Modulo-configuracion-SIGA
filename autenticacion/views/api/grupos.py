from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from rest_framework import permissions, viewsets
from django_filters import rest_framework as filters
from autenticacion.gateway.serializers.grupos import (
    SerializadorDeGruposEscritura,
    SerializadorDeGruposLectura,
)
from autenticacion.usecases import grupos as usecases
from autenticacion.gateway.manager import GruposManager


@extend_schema_view(
    create=extend_schema(tags=["Administración"], description="Crea un grupo"),
    retrieve=extend_schema(
        tags=["Administración"], description="Devuelve los detalles de un grupo"
    ),
    update=extend_schema(tags=["Administración"],
                         description="Actualiza un grupo"),
    partial_update=extend_schema(
        tags=["Administración"], description="Actualiza un grupo"
    ),
    destroy=extend_schema(tags=["Administración"],
                          description="Destruye un grupo"),
    list=extend_schema(
        tags=["Administración"],
        description="Lista los grupos",
        parameters=[OpenApiParameter(name="query", required=False, type=str)],
    ),
)
class VistasDeGrupos(
    usecases.CreateGrupo,
    usecases.DetailGrupo,
    usecases.UpdateGrupo,
    usecases.DeleteGrupo,
    usecases.ListGrupo,
    viewsets.GenericViewSet,
):
    """Lee y actualiza los grupos."""

    queryset = GruposManager().all()

    filter_backends = [filters.DjangoFilterBackend]

    filterset_fields = ["name"]

    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method in ["GET", "HEAD", "OPTIONS"]:
            return SerializadorDeGruposLectura
        return SerializadorDeGruposEscritura
