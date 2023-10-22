from polymorphic.managers import PolymorphicManager
from django.contrib.auth.models import Permission, Group

from autenticacion.models import Perfil, Usuario, Institucion
from comun.gateway import ModelManager


class PerfilManager(PolymorphicManager, ModelManager, model=Perfil):
    """Clase encargada de extender los managers predeterminados de Django para los perifles."""


class UsuarioManager(ModelManager, model=Usuario):
    """Clase encargada de extender los managers predeterminados de Django para los usuarios."""


class PermisosManager(ModelManager, model=Permission):
    """Clase encargada de extender los managers predeterminados de Django para los permisos."""


class GruposManager(ModelManager, model=Group):
    """Clase encargada de extender los managers predeterminados de Django para los grupos."""


class InstitucionesManager(ModelManager, model=Institucion):
    """Clase encargada de extender los managers predeterminados de Django para las instituciones."""
