"""
Este módulo de vistas está hecho con el propósito de redefinir la documentación(en inglés)
asociada a las vistas de autenticación y re implementar la lógica de algunas de ellas. 
El conjunto de clases que se implementan son autoexplicativas
"""
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from rest_framework import permissions, viewsets

from autenticacion.gateway.manager import UsuarioManager
from autenticacion.gateway.serializers import usuario as serializers
from autenticacion.usecases import usuarios as usecases
from comun.views import ByOperationSerializer, ByVersionSerializer


@extend_schema_view(
    create=extend_schema(tags=["Administración"],
                         description="Crea un usuario"),
    retrieve=extend_schema(
        tags=["Administración"], description="Devuelve los detalles de un usuario"
    ),
    update=extend_schema(tags=["Administración"],
                         description="Actualiza un usuario"),
    partial_update=extend_schema(
        tags=["Administración"], description="Actualiza un usuario"
    ),
    destroy=extend_schema(tags=["Administración"],
                          description="Destruye un usuario"),
    list=extend_schema(
        tags=["Administración"],
        description="Lista los usuarios",
        parameters=[OpenApiParameter(name="query", required=False, type=str)],
    ),
)
class VistasDeUsuarios(
    usecases.CreateUsuario,
    usecases.DetailUsuario,
    usecases.UpdateUsuario,
    usecases.DeleteUsuario,
    usecases.ListUsuario,
    ByOperationSerializer,
    ByVersionSerializer,
    viewsets.GenericViewSet,
):
    """Lee y actualiza los usuarios."""

    queryset = UsuarioManager().all()
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    serializer_class = {
        "v1": {
            "read": serializers.v1.SerializadorDeUsuarioLecturaConPerfil,
            "write": serializers.v1.SerializadorDeUsuarioEscritura,
        },
        "v2": {
            "read": serializers.v2.SerializadorDeUsuarioLecturaConPerfil,
            "write": serializers.v2.SerializadorDeUsuarioEscritura,
        },
    }
