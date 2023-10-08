from drf_spectacular.utils import extend_schema_serializer

from ..common import SerializadorDeUsuarioLecturaBase, MixingPerfil
from autenticacion.gateway.serializers.instituciones.serializer import SerializadorDeInstituciones


@extend_schema_serializer(component_name="SerializadorDeUsuarioLecturaV1")
class SerializadorDeUsuarioLectura(SerializadorDeUsuarioLecturaBase):
    class Meta:
        model = SerializadorDeUsuarioLecturaBase.Meta.model
        fields = SerializadorDeUsuarioLecturaBase.Meta.fields + ["last_name"]


@extend_schema_serializer(component_name="SerializadorDeUsuarioLecturaConPerfilV1")
class SerializadorDeUsuarioLecturaConPerfil(MixingPerfil, SerializadorDeUsuarioLectura):
    institucion = institucion = SerializadorDeInstituciones(
        read_only=True)

    class Meta:
        model = SerializadorDeUsuarioLecturaBase.Meta.model
        fields = (
            SerializadorDeUsuarioLecturaBase.Meta.fields
            + ["last_name", "institucion", 'id',
               'id_sexo',
               'id_municipio',
               'id_estructura',
               'nombre_completo',
               'ci',
               'solapin',
               'id_expediente',
               'id_categoria',
               'id_estructura_credencial',
               'id_persona_foto',
               'id_responsabilidad',
               'nombre_responsabilidad',
               'id_estructura_consejo',
               'id_categoria_residente',
               'id_tipo_curso',
               'id_apto',
               'id_origen',
               'codigo_solapin',
               'id_edificio',
               'id_carrera',
               'id_pais',
               'id_categoria_cientifica',
               'id_categoria_docente',
               'id_grupo']
            + MixingPerfil.Meta.fields
        )
