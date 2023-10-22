from rest_framework import mixins


class DetailInstitucion(mixins.RetrieveModelMixin):
    """Clase encargada de la obtención los datos de una Institucion."""
