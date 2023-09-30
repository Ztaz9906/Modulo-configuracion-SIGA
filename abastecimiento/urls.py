"""
URL configuration for abastecimiento project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

# Importamos 'path' para definir nuestras urls
# e 'include' para aquellas que definimos en las aplicaciones/módulos
from django.urls import include, path

admin.site.site_title = "Sistema de gestión de la DGT"
admin.site.site_header = "Sistema de gestión de la DGT"
admin.site.index_title = "Sistema de gestión de la DGT"
admin.site.site_url = settings.FRONTEND_URL

ui = [path("", include("documentacion.urls"))]
# noinspection SpellCheckingInspection
api = {
    "v1": [
        path("v1/", include("autenticacion.views.api.urls.v1")),
        path("api/docs/v1/", include("documentacion.urls")),
        path('v1/', include('cajero.urls')),
        path('v1/', include('cobro.urls')),
        path('v1/', include('reservacion.urls')),
        path('v1/', include('configuracion.urls')),
        path('v1/', include('base.urls')),
    ],
    "v2": [
        path("api/docs/v2/", include("documentacion.urls")),
        path("v2/", include("autenticacion.views.api.urls.v2")),
    ],
}

# Definimos las urls
urlpatterns = [
    path("api/docs/", include(ui)),
] + [path("", include((api[k], k))) for k in api]

urlpatterns = static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + urlpatterns  # type: ignore
urlpatterns = [
    path("admin/", admin.site.urls),
] + urlpatterns
