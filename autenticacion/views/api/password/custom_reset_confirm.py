from dj_rest_auth.views import PasswordResetConfirmView
from drf_spectacular.utils import extend_schema, extend_schema_view

from autenticacion.gateway.serializers.password import (
    custom_password_reset_confirm,
)
from autenticacion.usecases.password import custom_reset_confirm as usecases


@extend_schema_view(
    post=extend_schema(
        tags=["Autenticación"],
        description="Termina el proceso de recuperación de contraseñas.",
    )
)
class CustomPasswordResetConfirmView(
    usecases.PostCustomResetConfirm, PasswordResetConfirmView
):
    """Termina el flujo de reseteo de passwords."""

    serializer_class = (
        custom_password_reset_confirm.CustomPasswordResetConfirmSerializer
    )
