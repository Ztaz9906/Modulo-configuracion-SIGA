from django.urls import path, include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()

router.register(r'Reservacion_TbDelementosMostrar', TbDelementosMostrarViewSet)
router.register(r'Reservacion_TbDperiodoReservacion', TbDperiodoReservacionViewSet)
router.register(r'Reservacion_TbDreservacion', TbDreservacionViewSet)
router.register(r'Reservacion_TbDresponsableAreaPersonas', TbDresponsableAreaPersonasViewSet)
router.register(r'Reservacion_TbDresponsableReservacion', TbDresponsableReservacionViewSet)
router.register(r'Reservacion_TbHistorialReservacion', TbHistorialReservacionViewSet)
router.register(r'Reservacion_TbRreservacionPlato', TbRreservacionPlatoViewSet)
router.register(r'Reservacion_TbRticketReservacion', TbRticketReservacionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]