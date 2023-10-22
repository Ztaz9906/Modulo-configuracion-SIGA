from typing import Type
from dj_rest_auth.views import LoginView
from rest_framework import serializers


class PostCustomLoginBase(LoginView):
    """Clase encargada extender el comportamiento predeterminado de la clase LoginView() versión 2."""

    user_serializer_class: Type[serializers.ModelSerializer]

    def get_user_serializer_class(self):
        return self.user_serializer_class

    def post(self, request, *args, **kwargs):
        r = super().post(request, *args, **kwargs)
        if r.status_code == 200:
            userserializer = self.get_user_serializer_class()(
                self.serializer.validated_data["user"],
                context={"request": self.request},
            )
            r.data["user"] = userserializer.data
        try:
            del r.data["user"]["perfil"][
                "user"
            ]
        finally:
            return r
