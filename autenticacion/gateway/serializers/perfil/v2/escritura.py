from drf_spectacular.utils import extend_schema_serializer
from ..common import SerializadorDePerfilEscrituraBase


@extend_schema_serializer(component_name="SerializadorDePerfilEscrituraV2")
class SerializadorDePerfilEscritura(SerializadorDePerfilEscrituraBase):
    class Meta:
        model = SerializadorDePerfilEscrituraBase.Meta.model
        fields = SerializadorDePerfilEscrituraBase.Meta.fields
