from rest_framework import mixins


class DeleteInstitucion(mixins.DestroyModelMixin):
    """Clase encargada de la eliminación de los Instituciones."""
