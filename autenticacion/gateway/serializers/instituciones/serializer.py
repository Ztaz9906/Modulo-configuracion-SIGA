from autenticacion.models import Institucion
from rest_framework import serializers
from drf_spectacular.utils import extend_schema_serializer


@extend_schema_serializer(component_name="SerializadorDeInstituciones")
class SerializadorDeInstituciones(
    serializers.HyperlinkedModelSerializer
):
    """Clase encargada de serializar y deserializar las instituciones."""
    url = serializers.HyperlinkedIdentityField(
        view_name="institucion-detail#v1")

    class Meta:
        model = Institucion
        fields = ["id", "name", "active_modules",
                  "active", "url", "description"]
