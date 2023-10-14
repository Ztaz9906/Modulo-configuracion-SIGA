
from django.urls import path, include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()

router.register(r'torpedo', TbTorpedoViewSet)
router.register('personas', PersonaViewSet)
router.register(r'paises', TbNpaisViewSet)
router.register(r'provincias', TbNprovinciaViewSet)
router.register(r'edificios', TbNedificioViewSet)
router.register(r'categorias', TbNcategoriaViewSet)
router.register(r'aptos', TbNaptoViewSet)
router.register(r'sexos', TbNsexoViewSet)
router.register(r'carreras', TbNcarreraViewSet)
router.register(r'categorias_residentes', TbNcategoriaResidenteViewSet)
router.register(r'grupos', TbNgrupoViewSet)
router.register(r'categorias_docentes', TbNcategoriaDocenteViewSet)
router.register(r'municipios', TbNmunicipioViewSet)
router.register(r'responsabilidades', TbNresponsabilidadViewSet)
router.register(r'categorias_cientificas', TbNcategoriaCientificaViewSet)
router.register(r'estructuras', EstructuraViewSet)
router.register('tipo_estructuras', TipoEstructuraViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
