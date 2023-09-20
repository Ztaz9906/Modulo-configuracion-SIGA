
from django.urls import path, include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
################ Nuevo modelo #################################
router.register(r'Torpedo', TbTorpedoViewSet)
router.register(r'Persona', TbDpersonaViewSet)

################   final     #################################

urlpatterns = [
    path('', include(router.urls)),
]
