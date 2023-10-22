from dj_rest_auth.views import PasswordResetView
from drf_spectacular.utils import extend_schema, extend_schema_view

from autenticacion.gateway.serializers.password import custom_password_reset
from autenticacion.usecases.password import custom_reset as usecases


@extend_schema_view(
    post=extend_schema(
        tags=["Autenticación"],
        description="Inicia el proceso de recuperación de contraseña.",
    )
)
class CustomPasswordResetView(usecases.PostCustomReset, PasswordResetView):
    """Comienza el flujo de reseteo de passwords."""

    serializer_class = custom_password_reset.CustomPasswordResetSerializer
