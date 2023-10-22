from dj_rest_auth.views import UserDetailsView
from drf_spectacular.utils import extend_schema, extend_schema_view

from autenticacion.gateway.serializers import usuario as serializers
from autenticacion.usecases import custom_user_detail as usecases
from comun.views import ByOperationSerializer, ByVersionSerializer


@extend_schema_view(
    get=extend_schema(
        tags=["Autenticación"], description="Obtiene los detalles de un usuario"
    ),
    patch=extend_schema(
        tags=["Autenticación"],
        description="Actualiza parcialmente un usuario",
        deprecated=True,
    ),
    put=extend_schema(
        tags=["Autenticación"], description="Actualiza un usuario", deprecated=True
    ),
)
class CustomUserDetailView(
    usecases.GetCustomUserDetail,
    usecases.PatchCustomUserDetail,
    usecases.PutCustomUserDetail,
    ByOperationSerializer,
    ByVersionSerializer,
    UserDetailsView,
):
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
