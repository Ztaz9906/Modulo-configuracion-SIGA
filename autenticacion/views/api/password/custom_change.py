from dj_rest_auth.views import PasswordChangeView
from drf_spectacular.utils import extend_schema, extend_schema_view

from autenticacion.gateway.serializers.password import custom_password_change
from autenticacion.usecases.password import custom_change_view as usecases


@extend_schema_view(
    post=extend_schema(
        tags=["Autenticación"], description="Cambia la contraseña del v2 actual."
    )
)
class CustomPasswordChangeView(usecases.PostCustomChange, PasswordChangeView):
    """Cambia el password del v2 actual."""

    serializer_class = custom_password_change.CustomPasswordChangeSerializer
