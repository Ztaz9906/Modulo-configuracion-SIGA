from django.contrib.auth.models import Permission
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers


@extend_schema_serializer(component_name="SerializadorDePermisos")
class SerializadorDePermisos(
    serializers.HyperlinkedModelSerializer
):
    """Clase encargada de serializar y deserializar los permisos."""

    url = serializers.HyperlinkedIdentityField(view_name="permission-detail#v1")

    class Meta:
        model = Permission
        fields = ("id", "name", "url", "codename")
