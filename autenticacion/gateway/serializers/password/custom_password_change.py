from dj_rest_auth import serializers as auth_serializers
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample

CustomPasswordChangeSerializer = extend_schema_serializer(
    component_name="CambioDePassword",
    examples=[
        OpenApiExample(
            name="Cambio exitoso",
            value={
                "detail": "string",
            },
            response_only=True,
        )
    ],
)(auth_serializers.PasswordChangeSerializer)
