from django.conf import settings

PROFILES = getattr(settings, "PROFILES", None)
