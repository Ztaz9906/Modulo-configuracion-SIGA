from django.contrib.auth.models import Group
from rest_framework import serializers
from drf_spectacular.utils import extend_schema_serializer

from autenticacion.gateway.serializers import SerializadorDePermisos


@extend_schema_serializer(component_name="SerializadorDeGruposLectura")
class SerializadorDeGruposLectura(
    serializers.HyperlinkedModelSerializer
):
    """Clase encargada de serializar y deserializar los grupos."""

    url = serializers.HyperlinkedIdentityField(view_name="group-detail#v1")
    permissions = SerializadorDePermisos(many=True)

    class Meta:
        model = Group
        fields = ["id", "name", "permissions", "url"]
