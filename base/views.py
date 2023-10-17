
from .serializers import *
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from rest_framework import viewsets, permissions
from django_filters import rest_framework as filters
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from autenticacion.models.entities.torpedo import TbDpersonaTorpedo
from autenticacion.models.entities.persona import Persona


@extend_schema_view(
    create=extend_schema(tags=["Torpedo"],
                         description="Crea un torpedo"),
    retrieve=extend_schema(
        tags=["Torpedo"], description="Devuelve los detalles de un torpedo"
    ),
    update=extend_schema(tags=["Torpedo"],
                         description="Actualiza un torpedo"),
    partial_update=extend_schema(
        tags=["Torpedo"], description="Actualiza un torpedo"
    ),
    destroy=extend_schema(tags=["Torpedo"],
                          description="Destruye un torpedo"),
    list=extend_schema(
        tags=["Torpedo"],
        description="Lista los torpedos",
        parameters=[OpenApiParameter(name="query", required=False, type=str)],
    ),
)
class TbTorpedoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = TbDpersonaTorpedo.objects.none()
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


@extend_schema_view(
    create=extend_schema(tags=["Persona"],
                         description="Crea una persona"),
    retrieve=extend_schema(
        tags=["Persona"], description="Devuelve las detalles de un persona"
    ),
    update=extend_schema(tags=["Persona"],
                         description="Actualiza una persona"),
    partial_update=extend_schema(
        tags=["Persona"], description="Actualiza una persona"
    ),
    destroy=extend_schema(tags=["Persona"],
                          description="Destruye una persona"),
    list=extend_schema(
        tags=["Persona"],
        description="Lista las personas",
        parameters=[OpenApiParameter(name="query", required=False, type=str)],
    ),
)
class PersonaViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Persona.objects.none()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['nombre_completo', 'id_sexo', 'id_municipio', 'id_provincia', 'ci',
                        'id_categoria_residente', 'id_categoria', 'id_estructura',
                        'id_responsabilidad']

    def get_queryset(self):
        # Si el usuario es staff, devolver todas las personas.
        if self.request.user.is_staff:
            queryset = Persona.objects.all()
        else:
            # De lo contrario, filtrar por la institución del usuario.
            user_institucion = self.request.user.institucion
            queryset = Persona.objects.filter(institucion=user_institucion)

        # Luego, verificar los otros parámetros.
        id_configuracion_comensal = self.request.query_params.get('id_configuracion_comensal', None)
        exclude_param = self.request.query_params.get('exclude', 'false')
        include_param = self.request.query_params.get('include', 'flase')

        if id_configuracion_comensal:
            if exclude_param.lower() == 'true':
                queryset = queryset.exclude(id_configuracion_comensal=id_configuracion_comensal)
            else:
                queryset = queryset.filter(id_configuracion_comensal=include_param)

        return queryset

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PersonaSerializer
        else:
            return PersonaCreateSerializer

@extend_schema_view(
    create=extend_schema(tags=["Configuracion de Estruturas"],
                         description="Crea una Configuracion de Estruturas"),
    retrieve=extend_schema(
        tags=["Configuracion de Estruturas"], description="Devuelve las detalles de un Configuracion de Estruturas"
    ),
    update=extend_schema(tags=["Configuracion de Estruturas"],
                         description="Actualiza una Configuracion de Estruturas"),
    partial_update=extend_schema(
        tags=["Configuracion de Estruturas"], description="Actualiza una Configuracion de Estruturas"
    ),
    destroy=extend_schema(tags=["Configuracion de Estruturas"],
                          description="Destruye una Configuracion de Estruturas"),
    list=extend_schema(
        tags=["Configuracion de Estruturas"],
        description="Lista las Configuracion de Estruturas",
        parameters=[OpenApiParameter(name="query", required=False, type=str)],
    ),
)
class EstructuraViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = TbNestructura.objects.none()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['nombre_estructura', 'activo', "codigo_externo", 'codigo_area', 'id_tipo_estructura']

    def get_queryset(self):
        if self.request.user.is_staff:
            return TbNestructura.objects.all()
        user_institucion = self.request.user.institucion
        return TbNestructura.objects.filter(id_institucion=user_institucion)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TbNestructuraSerializer
        else:
            return TbNestructuraCreateSerializer


@extend_schema_view(
    create=extend_schema(tags=["Configuracion de Tipo de Estructuras"],
                         description="Crea una Configuracion de Tipo de Estructuras"),
    retrieve=extend_schema(
        tags=["Configuracion de Tipo de Estructuras"], description="Devuelve las detalles de un Configuracion de Tipo de Estructuras"
    ),
    update=extend_schema(tags=["Configuracion de Tipo de Estructuras"],
                         description="Actualiza una Configuracion de Tipo de Estructuras"),
    partial_update=extend_schema(
        tags=["Configuracion de Tipo de Estructuras"], description="Actualiza una Configuracion de Tipo de Estructuras"
    ),
    destroy=extend_schema(tags=["Configuracion de Tipo de Estructuras"],
                          description="Destruye una Configuracion de Tipo de Estructuras"),
    list=extend_schema(
        tags=["Configuracion de Tipo de Estructuras"],
        description="Lista las Configuracion de Tipo de Estructuras",
        parameters=[OpenApiParameter(name="query", required=False, type=str)],
    ),
)
class TipoEstructuraViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = TbNtipoEstructura.objects.none()
    serializer_class = TbNtipoEstructuraSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['nombre_tipo_estructura', 'activo']

    def get_queryset(self):
        if self.request.user.is_staff:
            return TbNtipoEstructura.objects.all()
        user_institucion = self.request.user.institucion
        return TbNtipoEstructura.objects.filter(id_institucion=user_institucion)


class ReadOnlyModelViewSet(mixins.RetrieveModelMixin,
                           mixins.ListModelMixin,
                           GenericViewSet):
    pass



def get_schema_config(model_name):
    def no_op_decorator(view_func):
        return view_func  # Decorador que no hace nada y simplemente devuelve la función original

    return {
        "retrieve": extend_schema(tags=["Nomecladores"], description=f"Devuelve los detalles de un {model_name}"),
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



