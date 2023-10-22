from rest_framework import serializers
from .models import *
from autenticacion.models.entities.torpedo import TbDpersonaTorpedo
from autenticacion.models.entities.persona import Persona
from reservacion.models import TbDresponsableAreaPersonas,TbDresponsableReservacion


class PersonaExcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = [
            'nombre_completo', 'ci', 'solapin', 'codigo_solapin', 'nombre_responsabilidad',
            'id_expediente', 'institucion'
        ]


class TbNpaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNpais
        fields = '__all__'


class TbNprovinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNprovincia
        fields = '__all__'


class TbNtipoEstructuraSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNtipoEstructura
        fields = '__all__'


class TbNestructuraSerializer(serializers.ModelSerializer):
    id_tipo_estructura = TbNtipoEstructuraSerializer(read_only=True)
    tiene_responsables_area = serializers.SerializerMethodField()
    tiene_responsables_reservacion = serializers.SerializerMethodField()

    class Meta:
        model = TbNestructura
        fields = (
            'id_estructura',
            'id_tipo_estructura',
            'id_institucion',
            'nombre_estructura',
            'codigo_externo',
            'codigo_area',
            'estructura_consejo',
            'estructura_credencial',
            'activo',
            'tiene_responsables_area',
            'tiene_responsables_reservacion'
        )

    def get_tiene_responsables_area(self, obj):
        return TbDresponsableAreaPersonas.objects.filter(id_estructura=obj).exists()

    def get_tiene_responsables_reservacion(self, obj):
        return TbDresponsableReservacion.objects.filter(id_estructura=obj).exists()


class TbNestructuraCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNestructura
        fields = '__all__'


class TbNedificioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNedificio
        fields = '__all__'


class TbNcategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNcategoria
        fields = '__all__'


class TbNaptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNapto
        fields = '__all__'


class TbNsexoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNsexo
        fields = '__all__'


class TbNcarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNcarrera
        fields = '__all__'


class TbNcategoriaResidenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNcategoriaResidente
        fields = '__all__'


class TbNgrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNgrupo
        fields = '__all__'


class TbNtipoCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNtipoCurso
        fields = '__all__'


class TbNcategoriaDocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNcategoriaDocente
        fields = '__all__'


class TbNorigenSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNorigen
        fields = '__all__'


class TbNmunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNmunicipio
        fields = '__all__'


class TbNresponsabilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNresponsabilidad
        fields = '__all__'


class TbNcategoriaCientificaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNcategoriaCientifica
        fields = '__all__'


class TbNparentescoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNparentesco
        fields = '__all__'
class TbRpersonaFamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbRpersonaFamiliar
        fields = '__all__'


class TbDpersonaTorpedoSerializer(serializers.ModelSerializer):
    id_sexo = TbNsexoSerializer(read_only=True)
    id_municipio = TbNmunicipioSerializer(read_only=True)
    id_provincia = TbNprovinciaSerializer(read_only=True)
    id_pais = TbNpaisSerializer(read_only=True)
    class Meta:
        model = TbDpersonaTorpedo
        fields = '__all__'


class TbDpersonaCreateTorpedoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbDpersonaTorpedo
        fields = '__all__'


class PersonaSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="persona-detail#v1")
    id_responsabilidad = TbNresponsabilidadSerializer(read_only=True)
    id_estructura = TbNestructuraSerializer(read_only=True)
    class Meta:
        model = Persona
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['url'] = self.fields['url'].to_representation(instance)
        return representation

class PersonaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

