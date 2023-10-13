from rest_framework import serializers
from rest_framework.serializers import ValidationError
from drf_spectacular.utils import extend_schema_serializer
from ..common import SerializadorDeUsuarioEscrituraBase


@extend_schema_serializer(component_name="SerializadorDeUsuarioEscrituraV1")
class SerializadorDeUsuarioEscritura(SerializadorDeUsuarioEscrituraBase):
    """Clase encargada de serializar y deserializar los usuarios."""
    class Meta:
        model = SerializadorDeUsuarioEscrituraBase.Meta.model
        fields = SerializadorDeUsuarioEscrituraBase.Meta.fields +['last_name']
