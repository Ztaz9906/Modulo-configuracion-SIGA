from django.urls import path, include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()

router.register(r'Reservacion_TbDelementosMostrar', TbDelementosMostrarViewSet)
router.register(r'Reservacion_TbDperiodoReservacion',
                TbDperiodoReservacionViewSet)
router.register(r'Reservacion_TbDresponsableAreaPersonas',
                TbDresponsableAreaPersonasViewSet)
router.register(r'Reservacion_TbDresponsableReservacion',
                TbDresponsableReservacionViewSet)
router.register(r'Reservacion_TbHistorialReservacion',
                TbHistorialReservacionViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
