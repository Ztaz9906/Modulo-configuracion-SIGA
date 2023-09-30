from django.core import mail
from rest_framework import serializers
from dj_rest_auth import serializers as auth_serializers


class _PasswordResetAsRegistrySerializerHelper(
    auth_serializers.PasswordResetSerializer
):
    url = serializers.URLField()

    def get_email_options(self):
        return super().get_email_options() | {
            "subject_template_name": "email/subject.txt",
            "email_template_name": "email/empty_body.html",
            "html_email_template_name": "email/user_registry.html",
            "use_https": True,
            "extra_email_context": {
                "url": self.data["url"],
                "site_name": "Tecnoschool",
            },
        }


def send_reset_password_email(
    email: str, callback_url: str | None = None, request=None
):
    """
    Send a reset password email
    Args:
        request: The request
        email: The target email
        callback_url: The url that must be called back with token info for proper reset flow
    """

    if callback_url and request:
        registry_helper = _PasswordResetAsRegistrySerializerHelper(
            data={"url": callback_url, "email": email},
            context={"request": request},
        )
        if registry_helper.is_valid(raise_exception=True):
            registry_helper.save()
    else:
        origin = request.META.get("HTTP_ORIGIN") if request else "Tecnoschool"
        message = f"Inicie el flujo de cambio de contraseña de Tecnoschool en {origin} para obtener un password válido."
        mail.EmailMessage(
            subject=f"Ha sido añadido como usuario a {origin}.",
            to=[email],
            body=message,
        ).send()
