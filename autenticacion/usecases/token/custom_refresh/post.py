from rest_framework_simplejwt.views import TokenRefreshView


class PostCustomRefresh(TokenRefreshView):
    """Clase encargada de extender el comportamiento predeterminado de la clase TokenRefreshView()."""
