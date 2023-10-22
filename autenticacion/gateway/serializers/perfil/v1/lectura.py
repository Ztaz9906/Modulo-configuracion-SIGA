from drf_spectacular.utils import extend_schema_serializer
from ..common import SerializadorDePerfilLecturaBase


@extend_schema_serializer(component_name="SerializadorDePerfilLecturaV1")
class SerializadorDePerfilLectura(SerializadorDePerfilLecturaBase):
    class Meta:
        model = SerializadorDePerfilLecturaBase.Meta.model
        # noinspection SpellCheckingInspection
        fields = SerializadorDePerfilLecturaBase.Meta.fields
