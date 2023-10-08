from rest_framework import serializers

from autenticacion import settings, models
from autenticacion.gateway.manager import GruposManager, PermisosManager
from autenticacion.gateway.serializers import SerializadorDePermisos
from autenticacion.gateway.serializers.grupos import (
    SerializadorDeGruposLectura,
)
from comun.serializers import polymorphic


# noinspection PyUnresolvedReferences
class MixingPerfil(serializers.Serializer):
    """Clase encargada de serializar y deserializar los usuarios con perfil."""

    perfil = serializers.SerializerMethodField(method_name="get_perfil")

    def get_perfil(self, obj) -> dict | None:
        version = "v1"
        request = self.context.get("request", {})
        if request != {}:
            version = request.version
        if not hasattr(obj, "perfil") or not settings.PROFILES[version]:
            return None

        serializer = polymorphic(models.Perfil, *settings.PROFILES[version])(
            getattr(obj, "perfil"), context=self.context
        )

        return serializer.data

    class Meta:
        fields = ["perfil"]


class SerializadorDeUsuarioLecturaBase(serializers.HyperlinkedModelSerializer):
    """Clase base utilizada en la serialización/deserialización de los usuarios."""

    url = serializers.HyperlinkedIdentityField(view_name="usuario-detail#v1")

    groups = SerializadorDeGruposLectura(many=True)
    user_permissions = SerializadorDePermisos(many=True)

    class Meta:
        model = models.Usuario
        fields = [
            "id",
            "username",
            "email",
            "is_staff",
            "groups",
            "user_permissions",
            "url",
        ]


class SerializadorDeUsuarioEscrituraBase(serializers.HyperlinkedModelSerializer):
    """Clase encargada de serializar y deserializar los usuarios."""

    groups = serializers.HyperlinkedRelatedField(
        view_name="group-detail#v1",
        many=True,
        queryset=GruposManager().all(),
        required=False,
    )

    user_permissions = serializers.HyperlinkedRelatedField(
        view_name="permission-detail#v1",
        many=True,
        queryset=PermisosManager().all(),
        required=False,
    )

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = models.Usuario
        fields = [
            "username",
            "email",
            'password',
            "is_staff",
            "groups",
            "user_permissions",
            "institucion",
        ]

