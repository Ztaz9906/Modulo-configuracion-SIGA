from rest_framework import mixins


class ListPermisos(mixins.ListModelMixin):
    """Clase encargada de la obtención de los datos de los permisos."""
