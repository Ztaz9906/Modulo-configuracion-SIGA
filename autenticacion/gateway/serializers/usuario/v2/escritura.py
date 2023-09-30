from drf_spectacular.utils import extend_schema_serializer
from ..common import SerializadorDeUsuarioEscrituraBase


@extend_schema_serializer(component_name="SerializadorDeUsuarioEscrituraV2")
class SerializadorDeUsuarioEscritura(SerializadorDeUsuarioEscrituraBase):
    class Meta:
        model = SerializadorDeUsuarioEscrituraBase.Meta.model
        fields = SerializadorDeUsuarioEscrituraBase.Meta.fields
