from drf_spectacular.utils import extend_schema_serializer
from ..common import SerializadorDeUsuarioLecturaBase, MixingPerfil


@extend_schema_serializer(component_name="SerializadorDeUsuarioLecturaV2")
class SerializadorDeUsuarioLectura(SerializadorDeUsuarioLecturaBase):
    class Meta:
        model = SerializadorDeUsuarioLecturaBase.Meta.model
        fields = SerializadorDeUsuarioLecturaBase.Meta.fields


@extend_schema_serializer(component_name="SerializadorDeUsuarioLecturaConPerfilV2")
class SerializadorDeUsuarioLecturaConPerfil(MixingPerfil, SerializadorDeUsuarioLectura):
    class Meta:
        model = SerializadorDeUsuarioLecturaBase.Meta.model
        fields = (
            SerializadorDeUsuarioLecturaBase.Meta.fields
            + MixingPerfil.Meta.fields
        )
