from autenticacion.gateway.serializers.usuario import v2 as serializers
from ..common import PostCustomLoginBase


class PostCustomLogin(PostCustomLoginBase):
    """Clase encargada extender el comportamiento predeterminado de la clase LoginView()."""

    user_serializer_class = serializers.SerializadorDeUsuarioLecturaConPerfil
