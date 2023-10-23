from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import QueryDict
from rest_framework.parsers import MultiPartParser

from comun.parser_excel import ExcelParser
from .serializers import *
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from rest_framework import viewsets, permissions
from django_filters import rest_framework as filters
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from autenticacion.models.entities.torpedo import TbDpersonaTorpedo
from autenticacion.models.entities.persona import Persona
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import openpyxl
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


class EstructuraFilter(filters.FilterSet):
    tiene_responsables_area = filters.BooleanFilter(field_name="tbdresponsableareapersonas", lookup_expr='isnull',
                                                    exclude=True)
    tiene_responsables_reservacion = filters.BooleanFilter(field_name="tbdresponsablereservacion", lookup_expr='isnull',
                                                           exclude=True)
    class Meta:
        model = TbNestructura
        fields = ['nombre_estructura', 'activo', "codigo_externo", 'codigo_area', 'id_tipo_estructura',
                  'tiene_responsables_area', 'tiene_responsables_reservacion']


@extend_schema_view(
    create=extend_schema(tags=["Configuracion de Areas"],
                         description="Crea una Configuracion de Areas"),
    retrieve=extend_schema(
        tags=["Configuracion de Areas"], description="Devuelve las detalles de un Configuracion de Areas"
    ),
    update=extend_schema(tags=["Configuracion de Areas"],
                         description="Actualiza una Configuracion de Areas"),
    partial_update=extend_schema(
        tags=["Configuracion de Areas"], description="Actualiza una Configuracion de Areas"
    ),
    destroy=extend_schema(tags=["Configuracion de Areas"],
                          description="Destruye una Configuracion de Areas"),
    list=extend_schema(
        tags=["Configuracion de Areas"],
        description="Lista las Configuracion de Areas",
        parameters=[OpenApiParameter(name="query", required=False, type=str)],
    ),
)
class EstructuraViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = TbNestructura.objects.none()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class  = EstructuraFilter

    def get_queryset(self):
        user_institucion = self.request.user.institucion
        return TbNestructura.objects.filter(id_institucion=user_institucion)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TbNestructuraSerializer
        else:
            return TbNestructuraCreateSerializer


@extend_schema_view(
    create=extend_schema(tags=["Configuracion de Tipo de Areas"],
                         description="Crea una Configuracion de Tipo de Areas"),
    retrieve=extend_schema(
        tags=["Configuracion de Tipo de Areas"], description="Devuelve las detalles de un Configuracion de Tipo de Areas"
    ),
    update=extend_schema(tags=["Configuracion de Tipo de Areas"],
                         description="Actualiza una Configuracion de Tipo de Areas"),
    partial_update=extend_schema(
        tags=["Configuracion de Tipo de Areas"], description="Actualiza una Configuracion de Tipo de Areas"
    ),
    destroy=extend_schema(tags=["Configuracion de Tipo de Areas"],
                          description="Destruye una Configuracion de Tipo de Areas"),
    list=extend_schema(
        tags=["Configuracion de Tipo de Areas"],
        description="Lista las Configuracion de Tipo de Areas",
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

@extend_schema_view(
    create=extend_schema(tags=["Exel"],
                         description="Carga un exel"),
)
class UploadExcelView(APIView):
    parser_classes = (ExcelParser, MultiPartParser)
    def post(self, request):

        # Verificar si los datos vienen en forma de QueryDict (posiblemente multipart)
        if isinstance(request.data, QueryDict) and 'file' in request.data:
            # El archivo fue enviado como 'multipart/form-data'
            uploaded_file = request.data['file']

            # Asegurarse de que id_institucion esté presente
            institucion = request.POST.get('institucion')
            print(institucion)
            if not institucion:
                return Response({'detail': 'Falta institucion.'}, status=status.HTTP_400_BAD_REQUEST)

            # Verificar si el uploaded_file es realmente un archivo
            if isinstance(uploaded_file, InMemoryUploadedFile):
                try:
                    # Procesa el archivo usando el ExcelParser manualmente
                    parser = ExcelParser()
                    data = parser.parse(uploaded_file)

                    # Agregar institucion a cada registro
                    for item in data:
                        item['institucion'] = institucion
                except Exception as e:
                    return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'detail': 'No se encontró archivo.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            data = request.data

        # Validar y guardar datos
        print(data)
        serializer = PersonaExcelSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'result': serializer.data, 'detail': 'Datos cargados correctamente.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
