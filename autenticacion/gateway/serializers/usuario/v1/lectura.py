from drf_spectacular.utils import extend_schema_serializer
from base.serializers import PersonaSerializer
from ..common import SerializadorDeUsuarioLecturaBase, MixingPerfil
from autenticacion.gateway.serializers.instituciones.serializer import SerializadorDeInstituciones


@extend_schema_serializer(component_name="SerializadorDeUsuarioLecturaV1")
class SerializadorDeUsuarioLectura(SerializadorDeUsuarioLecturaBase):
    class Meta:
        model = SerializadorDeUsuarioLecturaBase.Meta.model
        fields = SerializadorDeUsuarioLecturaBase.Meta.fields + ["last_name"]


@extend_schema_serializer(component_name="SerializadorDeUsuarioLecturaConPerfilV1")
class SerializadorDeUsuarioLecturaConPerfil(MixingPerfil, SerializadorDeUsuarioLectura):
    institucion = SerializadorDeInstituciones(
        read_only=True)
    persona = PersonaSerializer(read_only=True)

    class Meta:
        model = SerializadorDeUsuarioLecturaBase.Meta.model
        fields = (
            SerializadorDeUsuarioLecturaBase.Meta.fields
            + ["institucion", 'id', 'persona', 'last_name']
            + MixingPerfil.Meta.fields
        )
