from dj_rest_auth.views import LogoutView
from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiExample,
    inline_serializer,
)
from rest_framework import serializers

from autenticacion.usecases.session import custom_logout as usecases


@extend_schema_view(
    get=extend_schema(
        tags=["Autenticación"],
        request=None,
        responses=None,
        description="Confirma el proceso de borrado de la sesión del v2 actual",
        deprecated=True,
    ),  # TODO: Eliminar get ??
    post=extend_schema(
        tags=["Autenticación"],
        request=None,
        description="Confirma el borrado de la sesión del v2 actual",
        examples=[
            OpenApiExample(
                name="Logout válido",
                value={"detail": "string"},
                response_only=True,
                status_codes="200",
            )
        ],
        responses={
            200: inline_serializer(
                name="CustomLogoutSerializer",
                fields={
                    "data": serializers.CharField(),
                },
            )
        },
    ),
)
class CustomLogoutView(usecases.GetCustomLogout, usecases.PostCustomLogout, LogoutView):
    """Borra el token y la sesión asignada al v2 actual."""
