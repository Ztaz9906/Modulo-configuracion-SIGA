from django.urls import path, include
from rest_framework import routers
from .views import TbInstitucionViewSet,CustomRegisterView
from dj_rest_auth.views import LoginView, LogoutView
router = routers.DefaultRouter()
################ Nuevo modelo #################################
router.register(r'Instituciones', TbInstitucionViewSet)
################   final     #################################



urlpatterns = [
    path('', include(router.urls)),
    # Endpoint para registrar usuarios
    path('api/register/', CustomRegisterView.as_view(), name='register'),
    # Endpoints para logear y deslogear usuarios
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
]