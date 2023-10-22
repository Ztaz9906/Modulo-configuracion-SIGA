from dj_rest_auth import serializers as auth_serializers
from drf_spectacular.utils import extend_schema_serializer
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import exceptions as url_exceptions
from django.utils.translation import gettext_lazy as _
from rest_framework.serializers import ValidationError


# Get the UserModel
UserModel = get_user_model()


# Usamos el serializador del módulo auth_serializer y lo decoramos para que tenga otro nombre
# el resultado es una clase (no una instancia) nueva
@extend_schema_serializer(component_name="Login")
class CustomLoginSerializer(auth_serializers.LoginSerializer):
    """Clase encargada de serializar y deserializar los datos de autenticación."""

    def get_auth_user(self, username, email, password):
        """
        Retrieve the auth user from given POST payload by using
        either `allauth` auth scheme or bare Django auth scheme.

        Returns the authenticated user instance if credentials are correct,
        else `None` will be returned
        """
        if "allauth" in settings.INSTALLED_APPS:
            # When `is_active` of a user is set to False, allauth tries to return template html
            # which does not exist. This is the solution for it. See issue #264.
            try:
                return self.get_auth_user_using_allauth(username, email, password)
            except url_exceptions.NoReverseMatch:
                msg = _(
                    "Usuario o contraseña inválidos, por favor intente de nuevo.")
                raise ValidationError(msg)
        return self.get_auth_user_using_orm(username, email, password)

    def validate(self, attrs):
        username = attrs.get("username")
        email = attrs.get("email")
        password = attrs.get("password")
        user = self.get_auth_user(username, email, password)

        if not user:
            msg = _("Usuario o contraseña inválidos, por favor intente de nuevo.")
            raise ValidationError(msg)

        # Did we get back an active user?
        self.validate_auth_user_status(user)

        # If required, is the email verified?
        if "dj_rest_auth.registration" in settings.INSTALLED_APPS:
            self.validate_email_verification_status(user)

        attrs["user"] = user
        return attrs
