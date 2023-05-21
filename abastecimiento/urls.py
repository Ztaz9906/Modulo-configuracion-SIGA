"""abastecimiento URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from rest_framework.documentation import include_docs_urls
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Documentaticon API",
        default_version='v2',
        description="Documentaticon API para SIGA",
    ),
    validators=['flex'],
    public=True,
    permission_classes=[],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cajero.urls')),
    path('', include('cobro.urls')),
    path('', include('reservacion.urls')),
    path('', include('configuracion.urls')),
    path('', include('adminschema.urls')),
    path('docs/', include_docs_urls(title='API documentation')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-schema'),
]
