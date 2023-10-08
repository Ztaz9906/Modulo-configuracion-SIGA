
from .serializers import *
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from rest_framework import viewsets, permissions
from django_filters import rest_framework as filters
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from autenticacion.models.entities.torpedo import TbDpersonaTorpedo


@extend_schema_view(
    create=extend_schema(tags=["Torpedos"],
                         description="Crea una torpedo"),
    retrieve=extend_schema(
        tags=["Torpedos"], description="Devuelve los detalles de un torpedo"
    ),
    update=extend_schema(tags=["Torpedos"],
                         description="Actualiza un torpedo"),
    partial_update=extend_schema(
        tags=["Torpedos"], description="Actualiza un torpedo"
    ),
    destroy=extend_schema(tags=["Torpedos"],
                          description="Destruye un torpedo"),
    list=extend_schema(
        tags=["Torpedos"],
        description="Lista los torpedos",
        parameters=[OpenApiParameter(name="query", required=False, type=str)],
    ),
)
class TbTorpedoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = TbDpersonaTorpedo.objects.none()
    serializer_class = TbDpersonaTorpedoSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['nombre_completo', 'id_sexo','id_municipio','id_provincia','id_pais','ci']
    def get_queryset(self):
        if self.request.user.is_staff:
            return TbDpersonaTorpedo.objects.all()
        user_institucion = self.request.user.institucion
        return TbDpersonaTorpedo.objects.filter(id_institucion=user_institucion)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TbDpersonaTorpedoSerializer
        else:
            return TbDpersonaCreateTorpedoSerializer


class ReadOnlyModelViewSet(mixins.RetrieveModelMixin,
                           mixins.ListModelMixin,
                           GenericViewSet):
    pass

def get_schema_config(model_name):
    def no_op_decorator(view_func):
        return view_func  # Decorador que no hace nada y simplemente devuelve la función original

    return {
        "create": no_op_decorator,
        "retrieve": extend_schema(tags=["Nomecladores"], description=f"Devuelve los detalles de un {model_name}"),
        "update": no_op_decorator,
        "partial_update": no_op_decorator,
        "destroy": no_op_decorator,
        "list": extend_schema(tags=["Nomecladores"], description=f"Lista los {model_name}",
                              parameters=[OpenApiParameter(name="query", required=False, type=str)]),
    }


@extend_schema_view(**get_schema_config("Pais"))
class TbNpaisViewSet(ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = TbNpais.objects.all()
    serializer_class = TbNpaisSerializer


@extend_schema_view(**get_schema_config("Provincia"))
class TbNprovinciaViewSet(ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = TbNprovincia.objects.all()
    serializer_class = TbNprovinciaSerializer
@extend_schema_view(**get_schema_config("Edificio"))
class TbNedificioViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = TbNedificio.objects.all()
    serializer_class = TbNedificioSerializer
@extend_schema_view(**get_schema_config("Categoria"))
class TbNcategoriaViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = TbNcategoria.objects.all()
    serializer_class = TbNcategoriaSerializer
@extend_schema_view(**get_schema_config("Apartamento"))
class TbNaptoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = TbNapto.objects.all()
    serializer_class = TbNaptoSerializer
@extend_schema_view(**get_schema_config("Sexo"))
class TbNsexoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = TbNsexo.objects.all()
    serializer_class = TbNsexoSerializer
@extend_schema_view(**get_schema_config("Carrera"))
class TbNcarreraViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = TbNcarrera.objects.all()
    serializer_class = TbNcarreraSerializer
@extend_schema_view(**get_schema_config("Categoria de Residente"))
class TbNcategoriaResidenteViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = TbNcategoriaResidente.objects.all()
    serializer_class = TbNcategoriaResidenteSerializer
@extend_schema_view(**get_schema_config("Grupo"))
class TbNgrupoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = TbNgrupo.objects.all()
    serializer_class = TbNgrupoSerializer
@extend_schema_view(**get_schema_config("Categoria Docente"))
class TbNcategoriaDocenteViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = TbNcategoriaDocente.objects.all()
    serializer_class = TbNcategoriaDocenteSerializer
@extend_schema_view(**get_schema_config("Municipio"))
class TbNmunicipioViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = TbNmunicipio.objects.all()
    serializer_class = TbNmunicipioSerializer
@extend_schema_view(**get_schema_config("Responsabilidad"))
class TbNresponsabilidadViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = TbNresponsabilidad.objects.all()
    serializer_class = TbNresponsabilidadSerializer
@extend_schema_view(**get_schema_config("Categoria Cientifica"))
class TbNcategoriaCientificaViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = TbNcategoriaCientifica.objects.all()
    serializer_class = TbNcategoriaCientificaSerializer



