from django_filters import rest_framework as filters
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from rest_framework import viewsets, permissions

from .serializerGet import *
from .serializerPost import *


# ####################################################################### Pertenece a distibucion
# ################################


@extend_schema_view(
    create=extend_schema(tags=["Categoria"],
                         description="Crea una Categoria"),
    retrieve=extend_schema(
        tags=["Categoria"], description="Devuelve los detalles de una Categoria"
    ),
    update=extend_schema(tags=["Categoria"],
                         description="Actualiza una Categoria"),
    partial_update=extend_schema(
        tags=["Categoria"], description="Actualiza una Categoria"
    ),
    destroy=extend_schema(tags=["Categoria"],
                          description="Destruye una Categoria"),
    list=extend_schema(
        tags=["Categoria"],
        description="Lista las Categorias",
        parameters=[OpenApiParameter(name="query", required=False, type=str)],
    ),
)
class TbCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = {'name': ['exact'],
                        'active': ['exact']}
    def get_queryset(self):
        if self.request.user.is_staff:
            return TbCategory.objects.all()
        user_institution = self.request.user.institucion
        return TbCategory.objects.filter(id_institucion=user_institution)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TbCategorySerializer
        else:
            return TbCategoryCreateSerializer


@extend_schema_view(
    create=extend_schema(tags=["Clasificacion Evento"],
                         description="Crea una clasificacion Evento"),
    retrieve=extend_schema(
        tags=["Clasificacion Evento"], description="Devuelve los detalles de una clasificacion Evento"
    ),
    update=extend_schema(tags=["Clasificacion Evento"],
                         description="Actualiza un clasificacionEvento"),
    partial_update=extend_schema(
        tags=["Clasificacion Evento"], description="Actualiza una clasificacion Evento"
    ),
    destroy=extend_schema(tags=["Clasificacion Evento"],
                          description="Destruye una clasificacion Evento"),
    list=extend_schema(
        tags=["Clasificacion Evento"],
        description="Lista las clasificacion Eventos",
        parameters=[OpenApiParameter(name="query", required=False, type=str)],
    ),
)
class TbNclasificacionEventoViewSet(viewsets.ModelViewSet):
    queryset = TbNclasificacionEvento.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbNclasificacionEventoCreateSerializer
        else:
            return TbNclasificacionEventoSerializer


@extend_schema_view(
    create=extend_schema(tags=["Horario"],
                         description="Crea un horario"),
    retrieve=extend_schema(
        tags=["Horario"], description="Devuelve los detalles de un horario"
    ),
    update=extend_schema(tags=["Horario"],
                         description="Actualiza un horario"),
    partial_update=extend_schema(
        tags=["Horario"], description="Actualiza un horario"
    ),
    destroy=extend_schema(tags=["Horario"],
                          description="Destruye un horario"),
    list=extend_schema(
        tags=["Horario"],
        description="Lista los horarios",
        parameters=[OpenApiParameter(name="query", required=False, type=str)],
    ),
)
class TbNhorarioViewSet(viewsets.ModelViewSet):
    queryset = TbNhorario.objects.none()
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = {'nombre_horario': ['exact'],
                        'activo': ['exact']}
    def get_queryset(self):
        if self.request.user.is_staff:
            return TbNhorario.objects.all()
        user_institucion = self.request.user.institucion
        return TbNhorario.objects.filter(id_institucion=user_institucion)
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TbNhorarioSerializer
        else:
            return TbNhorarioCreateSerializer


@extend_schema_view(
    create=extend_schema(tags=["Evento"],
                         description="Crea un evento"),
    retrieve=extend_schema(
        tags=["Evento"], description="Devuelve los detalles de un evento"
    ),
    update=extend_schema(tags=["Evento"],
                         description="Actualiza un evento"),
    partial_update=extend_schema(
        tags=["Evento"], description="Actualiza un evento"
    ),
    destroy=extend_schema(tags=["Evento"],
                          description="Destruye un evento"),
    list=extend_schema(
        tags=["Evento"],
        description="Lista los eventos",
        parameters=[OpenApiParameter(name="query", required=False, type=str)],
    ),
)
class TbNeventoViewSet(viewsets.ModelViewSet):
    queryset = TbNevento.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = {'id_clasificacion_evento': ['exact'],
                        'activo': ['exact']}
    def get_queryset(self):
        if self.request.user.is_staff:
            return TbNevento.objects.all()
        user_institucion = self.request.user.institucion
        return TbNevento.objects.filter(id_institucion=user_institucion)
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TbNeventoSerializer
        return TbNeventoCreateSerializer


@extend_schema_view(
    create=extend_schema(tags=["Estructura"],
                         description="Crea una Estructura"),
    retrieve=extend_schema(
        tags=["Estructura"], description="Devuelve los detalles de una Estructura"
    ),
    update=extend_schema(tags=["Estructura"],
                         description="Actualiza un Estructura"),
    partial_update=extend_schema(
        tags=["Estructura"], description="Actualiza una Estructura"
    ),
    destroy=extend_schema(tags=["Estructura"],
                          description="Destruye una Estructura"),
    list=extend_schema(
        tags=["Estructura"],
        description="Lista las Estructuras",
        parameters=[OpenApiParameter(name="query", required=False, type=str)],
    ),
)
class TbStructureViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['name','initials','active']

    def get_queryset(self):
        # Crear un filtro base por institución o por usuario si es necesario
        if self.request.user.is_staff:
            base_query = TbStructure.objects.all()
        else:
            user_institucion = self.request.user.institucion
            base_query = TbStructure.objects.filter(id_institucion=user_institucion)

        # Si se está accediendo a la lista completa (action == 'list'),
        # filtrar solo aquellos que no tienen estructura padre (estructura_parent es nulo)
        if self.action == 'list':
            return base_query.filter(estructura_parent__isnull=True)

        # Para las otras acciones (retrieve, patch, delete, etc.), devolver el objeto
        # independientemente de si tiene un estructura_parent o no
        return base_query

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TbStructureSerializer
        else:
            return TbStructureCreateSerializer
######################################################################## Final ############################################

######################################################################## Abastecimiento con asset ###################################################


@extend_schema_view(
    create=extend_schema(tags=["Tipo de Producto"],
                         description="Crea un Tipo de Producto"),
    retrieve=extend_schema(
        tags=["Tipo de Producto"], description="Devuelve los detalles de un Tipo de Producto"
    ),
    update=extend_schema(tags=["Tipo de Producto"],
                         description="Actualiza un Tipo de Producto"),
    partial_update=extend_schema(
        tags=["Tipo de Producto"], description="Actualiza un Tipo de Producto"
    ),
    destroy=extend_schema(tags=["Tipo de Producto"],
                          description="Destruye un Tipo de Producto"),
    list=extend_schema(
        tags=["Tipo de Producto"],
        description="Lista los Tipos de Productos",
        parameters=[OpenApiParameter(name="query", required=False, type=str)],
    ),
)
class TbNtipoProductoViewSet(viewsets.ModelViewSet):
    queryset = TbNtipoProducto.objects.none()
    serializer_class = TbNtipoProductoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = {'nombre_tipo_producto': ['exact'],
                        'activo': ['exact']}

    def get_queryset(self):
        if self.request.user.is_staff:
            return TbNtipoProducto.objects.all()
        user_institucion = self.request.user.institucion
        return TbNtipoProducto.objects.filter(id_institucion=user_institucion)



@extend_schema_view(
    create=extend_schema(tags=["Unidad de Medida"],
                         description="Crea una Unidad de Medida"),
    retrieve=extend_schema(
        tags=["Unidad de Medida"], description="Devuelve los detalles de una Unidad de Medida"
    ),
    update=extend_schema(tags=["Unidad de Medida"],
                         description="Actualiza una Unidad de Medida"),
    partial_update=extend_schema(
        tags=["Unidad de Medida"], description="Actualiza una Unidad de Medida"
    ),
    destroy=extend_schema(tags=["Unidad de Medida"],
                          description="Destruye una Unidad de Medida"),
    list=extend_schema(
        tags=["Unidad de Medida"],
        description="Lista las Unidades de Medidas",
        parameters=[OpenApiParameter(name="query", required=False, type=str)],
    ),
)
class TbNunidadMedidaViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = {'nombre_unidad_medida': ['exact'],
                        'activo': ['exact'], 'clasificacion': ['exact']}

    def get_queryset(self):
        if self.request.user.is_staff:
            return TbNunidadMedida.objects.all()
        user_institucion = self.request.user.institucion
        return TbNunidadMedida.objects.filter(id_institucion=user_institucion)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbNunidadMedidaCreateSerializer
        else:
            return TbNunidadMedidaSerializer


@extend_schema_view(
    create=extend_schema(tags=["Clasificaion de Plato"],
                         description="Crea un Clasificaion de Plato"),
    retrieve=extend_schema(
        tags=["Clasificaion de Plato"], description="Devuelve los detalles de un Clasificaion de Plato"
    ),
    update=extend_schema(tags=["Clasificaion de Plato"],
                         description="Actualiza un Clasificaion de Plato"),
    partial_update=extend_schema(
        tags=["Clasificaion de Plato"], description="Actualiza un Clasificaion de Plato"
    ),
    destroy=extend_schema(tags=["Clasificaion de Plato"],
                          description="Destruye un Clasificaion de Plato"),
    list=extend_schema(
        tags=["Clasificaion de Plato"],
        description="Lista las Clasificaiones de Platos",
        parameters=[OpenApiParameter(name="query", required=False, type=str)],
    ),
)
class TbNclasificacionPlatoViewSet(viewsets.ModelViewSet):

    serializer_class = TbNclasificacionPlatoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = {'nombre_clasificacion_plato': ['exact'],
                        'activo': ['exact']}

    def get_queryset(self):
        if self.request.user.is_staff:
            return TbNclasificacionPlato.objects.all()
        user_institucion = self.request.user.institucion
        return TbNclasificacionPlato.objects.filter(id_institucion=user_institucion)
####### Empieza esquema asset ##########


@extend_schema_view(
    create=extend_schema(tags=["Producto"],
                         description="Crea un Producto"),
    retrieve=extend_schema(
        tags=["Producto"], description="Devuelve los detalles de un Producto"
    ),
    update=extend_schema(tags=["Producto"],
                         description="Actualiza un Producto"),
    partial_update=extend_schema(
        tags=["Producto"], description="Actualiza un Producto"
    ),
    destroy=extend_schema(tags=["Producto"],
                          description="Destruye un Producto"),
    list=extend_schema(
        tags=["Producto"],
        description="Lista los Productos",
        parameters=[OpenApiParameter(name="query", required=False, type=str)],
    ),
)
class TbDproductoViewSet(viewsets.ModelViewSet):
    queryset = TbDproducto.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = {'nombre_producto': ['exact'],
                        'id_tipo_producto': ['exact'], 'id_unidad_medida': ['exact']}

    def get_queryset(self):
        if self.request.user.is_staff:
            return TbDproducto.objects.all()
        user_institucion = self.request.user.institucion
        return TbDproducto.objects.filter(id_institucion=user_institucion)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TbDproductoSerializer
        else:
            return TbDproductoCreateSerializer


######### Termina esquema assets #########
class TbDconfiguracionProductoViewSet(viewsets.ModelViewSet):
    queryset = TbDconfiguracionProducto.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDconfiguracionProductoCreateSerializer
        else:
            return TbDconfiguracionProductoSerializer

######################################################################## Final #################################################

@extend_schema_view(
    create=extend_schema(tags=["Configuracciones de Accesos"],
                         description="Crea un Producto"),
    retrieve=extend_schema(
        tags=["Configuracciones de Accesos"], description="Devuelve los detalles de una Configuracciones de Accesos"
    ),
    update=extend_schema(tags=["Configuracciones de Accesos"],
                         description="Actualiza una Configuracciones de Accesos"),
    partial_update=extend_schema(
        tags=["Configuracciones de Accesos"], description="Actualiza una Configuracciones de Accesos"
    ),
    destroy=extend_schema(tags=["Configuracciones de Accesos"],
                          description="Destruye una Configuracciones de Accesos"),
    list=extend_schema(
        tags=["Configuracciones de Accesos"],
        description="Lista las Configuracciones de Accesoss",
        parameters=[OpenApiParameter(name="query", required=False, type=str)],
    ),
)
class TbDaccesoEventoSecundarioViewSet(viewsets.ModelViewSet):
    queryset = TbDaccesoEventoSecundario.objects.none()
    serializer_class = TbDaccesoEventoSecundarioSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        if self.request.user.is_staff:
            return TbDaccesoEventoSecundario.objects.all()
        user_institucion = self.request.user.institucion
        return TbDaccesoEventoSecundario.objects.filter(id_institucion=user_institucion)


@extend_schema_view(
    create=extend_schema(tags=["Asignar IP a Puerta"],
                         description="Crea un Asignar IP a Puerta"),
    retrieve=extend_schema(
        tags=["Asignar IP a Puerta"], description="Devuelve los detalles de un Asignar IP a Puerta"
    ),
    update=extend_schema(tags=["Asignar IP a Puerta"],
                         description="Actualiza un Asignar IP a Puerta"),
    partial_update=extend_schema(
        tags=["Asignar IP a Puerta"], description="Actualiza un Asignar IP a Puerta"
    ),
    destroy=extend_schema(tags=["Asignar IP a Puerta"],
                          description="Destruye un Asignar IP a Puerta"),
    list=extend_schema(
        tags=["Asignar IP a Puerta"],
        description="Lista los Asignar IP a Puerta",
        parameters=[OpenApiParameter(name="query", required=False, type=str)],
    ),
)
class TbDpersonaPuertaViewSet(viewsets.ModelViewSet):
    serializer_class = TbDpersonaPuertaSerializer
    queryset = TbDpersonaIPPuerta.objects.none()
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = {'id_puerta': ['exact'],
                        }
    def get_queryset(self):
        if self.request.user.is_staff:
            return TbDpersonaIPPuerta.objects.all()
        user_institucion = self.request.user.institucion
        return TbDpersonaIPPuerta.objects.filter(id_institucion=user_institucion)


@extend_schema_view(
    create=extend_schema(tags=["Solapin Perdido"],
                         description="Crea un Solapin Perdido"),
    retrieve=extend_schema(
        tags=["Solapin Perdido"], description="Devuelve los detalles de un Solapin Perdido"
    ),
    destroy=extend_schema(tags=["Solapin Perdido"],
                          description="Destruye un Solapin Perdido"),
    list=extend_schema(
        tags=["Solapin Perdido"],
        description="Lista los Solapin Perdido",
        parameters=[OpenApiParameter(name="query", required=False, type=str)],
    ),
)
class TbDsolapinPerdidoViewSet(viewsets.ModelViewSet):
    queryset = TbDsolapinPerdido.objects.none()
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = {'id_persona__id_sexo': ['exact'],
                        'id_persona__id_municipio': ['exact'],
                        'id_persona__id_pais': ['exact'],
                        'id_persona__ci': ['exact', 'icontains'],
                        'id_persona__nombre_completo': ['exact', 'icontains'],
                        'id_persona__solapin': ['exact', 'icontains'],
                        }
    def get_queryset(self):
        if self.request.user.is_staff:
            return TbDsolapinPerdido.objects.all()
        user_institucion = self.request.user.institucion
        return TbDsolapinPerdido.objects.filter(id_institucion=user_institucion)
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TbDsolapinPerdidoSerializer
        return TbDsolapinPerdidoCreateSerializer


@extend_schema_view(
    create=extend_schema(tags=["Estado de Tarjeta"],
                         description="Crea un Estado de Tarjeta"),
    retrieve=extend_schema(
        tags=["Estado de Tarjeta"], description="Devuelve los detalles de un Estado de Tarjeta"
    ),
    update=extend_schema(tags=["Estado de Tarjeta"],
                         description="Actualiza un Estado de Tarjeta"),
    partial_update=extend_schema(
        tags=["Estado de Tarjeta"], description="Actualiza un Estado de Tarjeta"
    ),
    destroy=extend_schema(tags=["Estado de Tarjeta"],
                          description="Destruye un Estado de Tarjeta"),
    list=extend_schema(
        tags=["Estado de Tarjeta"],
        description="Lista los Estado de Tarjeta",
        parameters=[OpenApiParameter(name="query", required=False, type=str)],
    ),
)
class TbNestadoTarjetaViewSet(viewsets.ModelViewSet):
    queryset = TbNestadoTarjeta.objects.none()
    serializer_class = TbNestadoTarjetaSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return TbNestadoTarjeta.objects.all()
        user_institucion = self.request.user.institucion
        return TbNestadoTarjeta.objects.filter(id_institucion=user_institucion)

@extend_schema_view(
    create=extend_schema(tags=["Tipo de Tarjeta"],
                         description="Crea un Tipo de Tarjeta"),
    retrieve=extend_schema(
        tags=["Tipo de Tarjeta"], description="Devuelve los detalles de un Tipo de Tarjeta"
    ),
    update=extend_schema(tags=["Tipo de Tarjeta"],
                         description="Actualiza un Tipo de Tarjeta"),
    partial_update=extend_schema(
        tags=["Tipo de Tarjeta"], description="Actualiza un Tipo de Tarjeta"
    ),
    destroy=extend_schema(tags=["Tipo de Tarjeta"],
                          description="Destruye un Tipo de Tarjeta"),
    list=extend_schema(
        tags=["Tipo de Tarjeta"],
        description="Lista los Tipo de Tarjeta",
        parameters=[OpenApiParameter(name="query", required=False, type=str)],
    ),
)
class TbNtipoTarjetaViewSet(viewsets.ModelViewSet):
    serializer_class = TbNtipoTarjetaSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = {'nombre_tipo_tarjeta': ['exact'],
                        'activo': ['exact']}

    def get_queryset(self):
        if self.request.user.is_staff:
            return TbNtipoTarjeta.objects.all()
        user_institucion = self.request.user.institucion
        return TbNtipoTarjeta.objects.filter(id_institucion=user_institucion)


@extend_schema_view(
    create=extend_schema(tags=["Tarjeta"],
                         description="Crea un Tarjeta"),
    retrieve=extend_schema(
        tags=["Tarjeta"], description="Devuelve los detalles de un Tarjeta"
    ),
    update=extend_schema(tags=["Tarjeta"],
                         description="Actualiza un Tarjeta"),
    partial_update=extend_schema(
        tags=["Tarjeta"], description="Actualiza un Tarjeta"
    ),
    destroy=extend_schema(tags=["Tarjeta"],
                          description="Destruye un Tarjeta"),
    list=extend_schema(
        tags=["Tarjeta"],
        description="Lista los Tarjeta",
        parameters=[OpenApiParameter(name="query", required=False, type=str)],
    ),
)
class TbDtarjetaAlimentacionViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = {'numero_serie': ['exact'],
                        'codigo': ['exact'] ,'id_estado_tarjeta': ['exact'],
                        'id_tipo_tarjeta': ['exact']}

    def get_queryset(self):
        if self.request.user.is_staff:
            return TbDtarjetaAlimentacion.objects.all()
        user_institucion = self.request.user.institucion
        return TbDtarjetaAlimentacion.objects.filter(id_institucion=user_institucion)
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TbDtarjetaAlimentacionSerializer
        else:
            return TbDtarjetaAlimentacionCreateSerializer

################################################################ Distribucion #################################################################


class TbNclasificacionDistribucionViewSet(viewsets.ModelViewSet):
    queryset = TbNclasificacionDistribucion.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbNclasificacionDistribucionCreateSerializer
        else:
            return TbNclasificacionDistribucionSerializer


class TbDdistribucionViewSet(viewsets.ModelViewSet):
    queryset = TbDdistribucion.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDdistribucionCreateSerializer
        else:
            return TbDdistribucionSerializer


class TbDpersonaDistribucionViewSet(viewsets.ModelViewSet):
    queryset = TbDpersonaDistribucion.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDpersonaDistribucionCreateSerializer
        else:
            return TbDpersonaDistribucionSerializer


class TbDtarjetaDistribucionViewSet(viewsets.ModelViewSet):
    queryset = TbDtarjetaDistribucion.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDtarjetaDistribucionCreateSerializer
        else:
            return TbDtarjetaDistribucionSerializer


class TbNreglaViewSet(viewsets.ModelViewSet):
    queryset = TbNregla.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbNreglaCreateSerializer
        else:
            return TbNreglaSerializer


class TbDvaloresReglaViewSet(viewsets.ModelViewSet):
    queryset = TbDvaloresRegla.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDvaloresReglaCreateSerializer
        else:
            return TbDvaloresReglaSerializer

# Revisar por q este modelo en la base de datos no tiene ninguna relacion con las tablas


class TbLastDistribucionViewSet(viewsets.ModelViewSet):
    queryset = TbLastDistribucion.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbLastDistribucionCreateSerializer
        else:
            return TbLastDistribucionSerializer


class TbNdiaSemanaViewSet(viewsets.ModelViewSet):
    queryset = TbNdiaSemana.objects.all()
    serializer_class = TbNdiaSemanaSerializer


class TbNrangoEventoViewSet(viewsets.ModelViewSet):
    queryset = TbNrangoEvento.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbNrangoEventoCreateSerializer
        else:
            return TbNrangoEventoSerializer


class TbRdistribucionReglaViewSet(viewsets.ModelViewSet):
    queryset = TbRdistribucionRegla.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbRdistribucionReglaCreateSerializer
        else:
            return TbRdistribucionReglaSerializer


class TbRestructuraReglaViewSet(viewsets.ModelViewSet):
    queryset = TbRestructuraRegla.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbRestructuraReglaCreateSerializer
        else:
            return TbRestructuraReglaSerializer


class TbReventoHorarioViewSet(viewsets.ModelViewSet):
    queryset = TbReventoHorario.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TbReventoHorarioSerializer
        else:
            return TbReventoHorarioCreateSerializer


class TbReventoRangoEventoViewSet(viewsets.ModelViewSet):
    queryset = TbReventoRangoEvento.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbReventoRangoEventoCreateSerializer
        else:
            return TbReventoRangoEventoSerializer


# revisar por que esta sin ralacion alguna ninnguno de estos id


################################################################    Fin      #################################################################

################################################################ Esquema cajero ##############################################################


class TbDconfiguracionTarjetaViewSet(viewsets.ModelViewSet):
    queryset = TbDconfiguracionTarjeta.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbDconfiguracionTarjetaCreateSerializer
        else:
            return TbDconfiguracionTarjetaSerializer


class TbNestadoMovimientoAsignacionViewSet(viewsets.ModelViewSet):
    queryset = TbNestadoMovimientoAsignacion.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbNestadoMovimientoAsignacionCreateSerializer
        else:
            return TbNestadoMovimientoAsignacionSerializer


class TbMovimientoAsignacionViewSet(viewsets.ModelViewSet):
    queryset = TbMovimientoAsignacion.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbMovimientoAsignacionCreateSerializer
        else:
            return TbMovimientoAsignacionSerializer


class TbRpersonaTarjetaViewSet(viewsets.ModelViewSet):
    queryset = TbRpersonaTarjeta.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TbRpersonaTarjetaCreateSerializer
        else:
            return TbRpersonaTarjetaSerializer
########################################################################## Fin ###############################################################################
