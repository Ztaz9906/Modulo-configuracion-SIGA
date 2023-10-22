"""
Módulo necesario para definir la aplicación de autenticación (auth)
"""
from django.apps import AppConfig


# noinspection PyMissingOrEmptyDocstring
class AutenticacionConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "autenticacion"
    verbose_name = "Autenticación"

    def ready(self) -> None:
        """Función encargada de registrar los modelos en el panel de admin durante el inicio de la app."""

        from autenticacion.views.admin import setup

        setup.initialize()
