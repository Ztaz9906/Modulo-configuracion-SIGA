from django.contrib.auth.models import Group
from rest_framework import serializers
from drf_spectacular.utils import extend_schema_serializer

from autenticacion.gateway.manager import PermisosManager


@extend_schema_serializer(component_name="SerializadorDeGrupoEscritura")
class SerializadorDeGruposEscritura(serializers.HyperlinkedModelSerializer):
    """Clase encargada de serializar y deserializar los grupos."""

    permissions = serializers.HyperlinkedRelatedField(
        view_name="permission-detail#v1",
        many=True,
        queryset=PermisosManager().all(),
    )

    class Meta:
        model = Group
        fields = ["id", "name", "permissions"]
