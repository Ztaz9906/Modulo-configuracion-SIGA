from rest_framework import mixins


class DeleteUsuario(mixins.DestroyModelMixin):
    """Clase encargada de la eliminación de usuarios."""
