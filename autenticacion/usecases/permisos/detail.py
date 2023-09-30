from rest_framework import mixins


class DetailPermisos(mixins.RetrieveModelMixin):
    """Clase encargada de la obtención de los datos de un permiso."""
