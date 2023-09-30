from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from rest_framework import permissions, viewsets

from autenticacion.usecases import permisos as usecases
from autenticacion.gateway import serializers
from autenticacion.gateway.manager import PermisosManager


@extend_schema_view(
    retrieve=extend_schema(
        tags=["Administración"], description="Devuelve los detalles de un permiso"
    ),
    list=extend_schema(
        tags=["Administración"],
        description="Lista los permisos",
        parameters=[OpenApiParameter(name="query", required=False, type=str)],
    ),
)
class VistasDePermisos(
    usecases.DetailPermisos, usecases.ListPermisos, viewsets.GenericViewSet
):
    """Lee y actualiza los permisos."""

    queryset = PermisosManager().all()
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    serializer_class = serializers.SerializadorDePermisos
