"""
URLS asociadas a la autenticación
"""

# Importamos 'path' para definir nuestras urls
from django.urls import include, path
from rest_framework import routers

# Importamos las vistas de autenticación
from autenticacion.views.api.session import login
from autenticacion.views.api.user import (
    CustomUserDetailView,
    VistasDeUsuarios,
)

router = routers.SimpleRouter()
router.register("usuarios", VistasDeUsuarios)

# Definimos las urls
urlpatterns = [
    path("api/login/", login("v2").as_view(), name="api-login"),
    path("api/user/", CustomUserDetailView.as_view(), name="api-user-details"),
    path("api/management/", include(router.urls)),
]
