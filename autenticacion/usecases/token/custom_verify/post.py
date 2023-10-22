from rest_framework_simplejwt.views import TokenVerifyView


class PostCustomVerify(TokenVerifyView):
    """Clase encargada de extender el comportamiento predeterminado de la clase TokenVerifyView()."""
