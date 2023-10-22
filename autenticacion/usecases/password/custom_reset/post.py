from dj_rest_auth.views import PasswordResetView


class PostCustomReset(PasswordResetView):
    """Clase encargada de extender el comportamieneto predeterminado de la clase PasswordResetView()."""
