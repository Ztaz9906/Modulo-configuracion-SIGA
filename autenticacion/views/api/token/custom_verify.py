from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiExample,
    inline_serializer,
)
from rest_framework import serializers
from rest_framework_simplejwt.views import TokenVerifyView

from autenticacion.usecases.token import custom_verify as usecases


@extend_schema_view(
    post=extend_schema(
        tags=["Autenticación"],
        description="Retorna la validez del token.",
        examples=[
            OpenApiExample(
                name="Token Válido", value={}, response_only=True, status_codes="200"
            ),
            OpenApiExample(
                name="Token Invalido",
                value={
                    "detail": "Token is invalid or expired",
                    "code": "token_not_valid",
                },
                response_only=True,
                status_codes="400",
            ),
        ],
        responses={
            200: inline_serializer(
                name="ValidTokenSerializer",
                fields={
                    "data": serializers.CharField(),
                },
            ),
            400: inline_serializer(
                name="InvalidTokenSerializer",
                fields={
                    "detail": serializers.CharField(),
                    "code": serializers.CharField(),
                },
            ),
        },
    )
)
class CustomTokenVerifyView(usecases.PostCustomVerify, TokenVerifyView):
    """Recibe un token y devuelve si es válido o no. Esta vista no provee
    ninguna información extra sobre el token."""
