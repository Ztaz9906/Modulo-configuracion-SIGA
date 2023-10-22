from typing import Type
from dj_rest_auth.views import LoginView, GenericAPIView
from drf_spectacular.utils import extend_schema, extend_schema_view

from autenticacion.gateway import serializers
from autenticacion.usecases.session import custom_login as usecases


def login(version) -> Type[GenericAPIView]:
    @extend_schema_view(
        post=extend_schema(
            tags=["Autenticación"],
            description=f"Inicia la sesión para el usuario de la versión {version}",
        ),
    )
    class CustomLoginView(
        getattr(getattr(usecases, version), "PostCustomLogin", object), LoginView
    ):
        f"""Comprueba las credenciales y retorna el token apropiado si
        las credenciales son válidas, además habilita una sesión para el usuario de la versión {version}.
        """

        serializer_class = serializers.CustomLoginSerializer

    return CustomLoginView
