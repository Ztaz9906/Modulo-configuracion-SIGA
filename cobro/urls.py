from django.urls import path, include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()

router.register(r'Cobro_TbNtipoCobro', TbNtipoCobroViewSet)
router.register('Cobro_TbNconfiguracionCobro', TbNconfiguracionCobroViewSet)
router.register('Cobro_TbNvaloresConfiguracionCobro', TbNvaloresConfiguracionCobroViewSet, basename='valores_configuracio_cobro')

urlpatterns = [
    path('', include(router.urls)),
]