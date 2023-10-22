import unidecode
from django.contrib import auth
from django.db import transaction
from rest_framework import serializers

from autenticacion import models
from autenticacion.gateway.manager import (
    GruposManager,
    PermisosManager,
    UsuarioManager,
    Usuario,
)
from comun.email import send_reset_password_email


class SerializadorDePerfilEscrituraBase(serializers.HyperlinkedModelSerializer):
    """Clase encargada de serializar y deserializar los perfiles."""

    # region relacionada con el v2
    correo = serializers.EmailField(
        required=True, write_only=True, allow_null=False, allow_blank=False
    )
    nombre = serializers.CharField(required=True, write_only=True)
    foto = serializers.ImageField(required=False, write_only=True)
    groups = serializers.HyperlinkedRelatedField(
        view_name="group-detail#v1",
        many=True,
        queryset=GruposManager().all(),
        write_only=True,
        required=False,
    )
    # noinspection SpellCheckingInspection

    user_permissions = serializers.HyperlinkedRelatedField(
        view_name="permission-detail#v1",
        many=True,
        queryset=PermisosManager().all(),
        write_only=True,
        required=False,
    )
    # endregion

    url_cambio_password = serializers.CharField(required=False, write_only=True)

    # noinspection PyMethodMayBeStatic

    def validate(self, attrs):
        correo = attrs.get("correo", None)
        try:
            obj = UsuarioManager().get(email=correo)
        except Usuario.DoesNotExist:
            return super().validate(attrs)
        if self.instance and obj.id == self.instance.user.id:
            return super().validate(attrs)
        else:
            raise serializers.ValidationError("Ya existe un usuario con ese correo.")

    # noinspection SpellCheckingInspection
    @transaction.atomic
    def update(self, instance, validated_data):
        user = auth.get_user_model().objects.get(id=instance.user.id)

        user.email = validated_data.pop("correo", instance.user.email)
        user.first_name = validated_data.pop("nombre", instance.user.first_name)

        user.foto = validated_data.pop("foto", instance.user.foto)

        instance.user.groups.set(
            validated_data.pop("groups", instance.user.groups.all())
        )
        instance.user.user_permissions.set(
            validated_data.pop("user_permissions", instance.user.user_permissions.all())
        )

        # Actualizando instancia para devolver response body actualizada.
        instance.user.first_name = user.first_name
        instance.user.email = user.email
        instance.user.foto = user.foto

        user.save()

        return instance

    @transaction.atomic
    def create(self, validated_data):
        username = unidecode.unidecode(validated_data.get("nombre")).strip().lower()
        count = 0

        while (
            auth.get_user_model()
            .objects.filter(username=(username + (str(count) if count else "")))
            .exists()
        ):
            count += 1
        username = username + (str(count) if count else "")

        user = auth.get_user_model().objects.create(
            username=username,
            email=validated_data.pop("correo"),
            first_name=validated_data.pop("nombre"),
            apellido_paterno="",
            apellido_materno="",
            foto=validated_data.pop("foto", None),
        )
        user.groups.set(validated_data.pop("groups", []))
        user.user_permissions.set(validated_data.pop("user_permissions", []))
        user.set_unusable_password()
        validated_data["user"] = user
        callback_url = validated_data.pop("url_cambio_password", None)
        created = super().create(validated_data)
        send_reset_password_email(user.email, callback_url, self.context["request"])
        return created

    class Meta:
        model = models.Perfil
        fields = [
            "correo",
            "nombre",
            "foto",
            "groups",
            "user_permissions",
            "url_cambio_password",
            "url_cambio_password",
        ]


class SerializadorDePerfilLecturaBase(serializers.HyperlinkedModelSerializer):
    """Clase encargada de serializar y deserializar los perfiles."""

    class Meta:
        model = models.Perfil
        fields = ["id"]
