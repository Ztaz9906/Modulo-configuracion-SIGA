from dj_rest_auth.jwt_auth import CookieTokenRefreshSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework_simplejwt.views import TokenRefreshView

from autenticacion.usecases.token import custom_refresh as usecases


@extend_schema_view(
    post=extend_schema(
        tags=["Autenticación"],
        description="Intenta refrescar un token de autenticación.",
    ),
)
class CustomTokenRefreshView(
    usecases.PostCustomRefresh, usecases.FinalizeResponse, TokenRefreshView
):
    """Intenta refrescar un token de autenticación."""

    serializer_class = CookieTokenRefreshSerializer
