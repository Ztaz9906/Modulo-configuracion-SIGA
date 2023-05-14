from django.urls import path, include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()

router.register(r'Configuracion_TbDavisos', TbDavisosViewSet)
router.register(r'Configuracion_TbDconfiguracionCobro', TbDconfiguracionCobroViewSet)
router.register(r'Configuracion_TbDconfiguracionElastic', TbDconfiguracionElasticViewSet)
router.register(r'Configuracion_TbDconfiguracionEventoAcceso', TbDconfiguracionEventoAccesoViewSet)
router.register(r'Configuracion_TbDconfiguracionPersona', TbDconfiguracionPersonaViewSet)
router.register(r'Configuracion_TbDconfiguracionProceso', TbDconfiguracionProcesoViewSet)
router.register(r'Configuracion_TbDconfiguracionRabbitmq', TbDconfiguracionRabbitmqViewSet)
router.register(r'Configuracion_TbDcron', TbDcronViewSet)
router.register(r'Configuracion_TbDdatosContacto', TbDdatosContactoViewSet)
router.register(r'Configuracion_TbDplanificacionMenu', TbDplanificacionMenuViewSet)
router.register(r'Configuracion_TbDvaloresConfiguracionCobro', TbDvaloresConfiguracionCobroViewSet)
router.register(r'Configuracion_TbDvaloresConfiguracionEventoAcceso', TbDvaloresConfiguracionEventoAccesoViewSet)
router.register(r'Configuracion_TbDvaloresConfiguracionPersona', TbDvaloresConfiguracionPersonaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]