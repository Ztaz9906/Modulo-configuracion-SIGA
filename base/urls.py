
from django.urls import path, include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()

router.register(r'torpedo', TbTorpedoViewSet)
router.register(r'paises', TbNpaisViewSet)
router.register(r'provincias', TbNprovinciaViewSet)
router.register(r'edificios', TbNedificioViewSet)
router.register(r'categorias', TbNcategoriaViewSet)
router.register(r'aptos', TbNaptoViewSet)
router.register(r'sexos', TbNsexoViewSet)
router.register(r'carreras', TbNcarreraViewSet)
router.register(r'categorias-residentes', TbNcategoriaResidenteViewSet)
router.register(r'grupos', TbNgrupoViewSet)
router.register(r'categorias-docentes', TbNcategoriaDocenteViewSet)
router.register(r'municipios', TbNmunicipioViewSet)
router.register(r'responsabilidades', TbNresponsabilidadViewSet)
router.register(r'categorias-cientificas', TbNcategoriaCientificaViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
