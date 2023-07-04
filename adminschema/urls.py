from django.urls import path, include
from rest_framework import routers
from .views import TbInstitucionViewSet, TbUserViewSet, GroupViewSet, CustomLoginView
from dj_rest_auth.urls import LogoutView
router = routers.DefaultRouter()
################ Nuevo modelo #################################
router.register(r'Instituciones', TbInstitucionViewSet)
################   final     #################################
router.register("roles", GroupViewSet)

router.register("Users", TbUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # Endpoints para logear y deslogear usuarios
    path('login/', CustomLoginView.as_view()),
    path('logout/', LogoutView.as_view()),
]
