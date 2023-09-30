from dj_rest_auth.jwt_auth import (
    set_jwt_access_cookie,
    set_jwt_refresh_cookie,
)
from django.utils import timezone
from rest_framework_simplejwt.settings import api_settings as jwt_settings


class FinalizeResponse:
    # TODO: Comentar

    def finalize_response(self, request, response, *args, **kwargs):
        if response.status_code == 200 and "access" in response.data:
            set_jwt_access_cookie(response, response.data["access"])
            response.data["access_token_expiration"] = (
                timezone.now() + jwt_settings.ACCESS_TOKEN_LIFETIME  # type: ignore
            )
        if response.status_code == 200 and "refresh" in response.data:
            set_jwt_refresh_cookie(response, response.data["refresh"])
        # noinspection PyUnresolvedReferences
        return super().finalize_response(request, response, *args, **kwargs)
