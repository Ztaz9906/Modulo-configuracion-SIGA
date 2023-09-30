"""
URLS asociadas a la autenticación
"""

# Importamos 'path' para definir nuestras urls
from django.urls import include, path
from rest_framework import routers

from autenticacion.views.api.grupos import VistasDeGrupos
from autenticacion.views.api.instituciones import VistasDeInstituciones
from autenticacion.views.api.password import (
    CustomPasswordChangeView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetView,
)
from autenticacion.views.api.permisos import VistasDePermisos

# Importamos las vistas de autenticación
from autenticacion.views.api.session import login, CustomLogoutView
from autenticacion.views.api.token import (
    CustomTokenRefreshView,
    CustomTokenVerifyView,
)
from autenticacion.views.api.user import (
    CustomUserDetailView,
    VistasDeUsuarios,
)

router = routers.SimpleRouter()
router.register("permisos", VistasDePermisos)
router.register("grupos", VistasDeGrupos)
router.register("usuarios", VistasDeUsuarios)
router.register("instituciones_nuevo", VistasDeInstituciones)
# Definimos las urls
urlpatterns = [
    path("api/login/", login("v1").as_view(), name="api-login"),
    path("api/logout/", CustomLogoutView.as_view(), name="api-logout"),
    path("api/user/", CustomUserDetailView.as_view(), name="api-user-details"),
    path(
        "api/password/change/",
        CustomPasswordChangeView.as_view(),
        name="rest_password_change",
    ),
    path("api/token/verify/", CustomTokenVerifyView.as_view(), name="token-verify"),
    path("api/token/refresh/", CustomTokenRefreshView.as_view(), name="token-refresh"),
    path(
        "api/password/reset/",
        CustomPasswordResetView.as_view(),
        name="api-password-reset",
    ),
    path(
        "api/password/reset/confirm/",
        CustomPasswordResetConfirmView.as_view(),
        name="api-password-reset-confirm",
    ),
    path("api/management/", include(router.urls)),
]
