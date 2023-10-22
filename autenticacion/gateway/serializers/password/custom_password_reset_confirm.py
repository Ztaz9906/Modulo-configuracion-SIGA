from dj_rest_auth import serializers as auth_serializers
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample


@extend_schema_serializer(
    component_name="ConfirmaciónDeReseteoDePassword",
    examples=[
        OpenApiExample(
            name="Reset exitoso",
            value={
                "detail": "string",
            },
            response_only=True,
        )
    ],
)
class CustomPasswordResetConfirmSerializer(
    auth_serializers.PasswordResetConfirmSerializer
):
    # TODO: Comentar
    ...
