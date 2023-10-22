from dj_rest_auth import serializers as auth_serializers
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from rest_framework import serializers


@extend_schema_serializer(
    component_name="ReseteoDePassword",
    examples=[
        OpenApiExample(
            name="Reset comenzado",
            value={
                "detail": "string",
            },
            response_only=True,
        )
    ],
)
class CustomPasswordResetSerializer(auth_serializers.PasswordResetSerializer):
    # TODO: Comentar

    url = serializers.URLField()

    def get_email_options(self):
        return super().get_email_options() | {
            "subject_template_name": "email/subject.txt",
            "email_template_name": "email/empty_body.html",
            "html_email_template_name": "email/password_change.html",
            "use_https": True,
            "extra_email_context": {
                "url": self.data["url"],
                "site_name": "Tecnoschool",
            },
        }
