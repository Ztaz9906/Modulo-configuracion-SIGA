from django.urls import path, include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()

router.register(r'Cobro_TbTipoRegla', TbTipoReglaViewSet)
router.register(r'Cobro_TbNestadoImportacion', TbNestadoImportacionViewSet)
router.register(r'Cobro_TbDimportacion', TbDimportacionViewSet)
router.register(r'Cobro_TbDimportaciones', TbDimportacionesViewSet)
router.register(r'Cobro_TbDimportacionRegistro', TbDimportacionRegistroViewSet)
router.register(r'Cobro_TbDpersonaRegla', TbDpersonaReglaViewSet)
router.register(r'Cobro_TbDreglaCobro', TbDreglaCobroViewSet)
router.register(r'Cobro_TbNtipoCobro', TbNtipoCobroViewSet)
router.register(r'Cobro_TbRfechaExcluida', TbRfechaExcluidaViewSet)
router.register(r'Cobro_TbRimportacionReservacion', TbRimportacionReservacionViewSet)
router.register(r'Cobro_TbRpersonaExcluidaCobro', TbRpersonaExcluidaCobroViewSet)

urlpatterns = [
    path('', include(router.urls)),
]