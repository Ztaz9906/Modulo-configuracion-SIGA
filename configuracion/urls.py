from django.urls import path, include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()


router.register(r'Configuracion_TbDconfiguracionProceso',
                TbDconfiguracionProcesoViewSet)
router.register(r'Configuracion_TbDdatosContacto', TbDdatosContactoViewSet)
router.register(r'Configuracion_TbDconfiguracionPersona',
                TbDconfiguracionPersonaViewSet)
router.register(r'Configuracion_TbDvaloresConfiguracionPersona',
                TbDvaloresConfiguracionPersonaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
