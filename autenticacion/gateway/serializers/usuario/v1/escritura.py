from rest_framework import serializers
from rest_framework.serializers import ValidationError
from drf_spectacular.utils import extend_schema_serializer
from ..common import SerializadorDeUsuarioEscrituraBase


@extend_schema_serializer(component_name="SerializadorDeUsuarioEscrituraV1")
class SerializadorDeUsuarioEscritura(SerializadorDeUsuarioEscrituraBase):
    """Clase encargada de serializar y deserializar los usuarios."""
    class Meta:
        model = SerializadorDeUsuarioEscrituraBase.Meta.model
        fields = SerializadorDeUsuarioEscrituraBase.Meta.fields + ['id',
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
