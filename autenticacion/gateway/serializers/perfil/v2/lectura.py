from drf_spectacular.utils import extend_schema_serializer
from ..common import SerializadorDePerfilLecturaBase


@extend_schema_serializer(component_name="SerializadorDePerfilLecturaV2")
class SerializadorDePerfilLectura(SerializadorDePerfilLecturaBase):
    class Meta:
        model = SerializadorDePerfilLecturaBase.Meta.model
        fields = SerializadorDePerfilLecturaBase.Meta.fields
