from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from rest_framework import viewsets
from django_filters import rest_framework as filters
from autenticacion.gateway.serializers.instituciones import SerializadorDeInstituciones
from autenticacion.usecases import instituciones as usecases
from autenticacion.gateway.manager import InstitucionesManager


@extend_schema_view(
    create=extend_schema(tags=["Instituciones"],
                         description="Crea una Institucion"),
    retrieve=extend_schema(
        tags=["Instituciones"], description="Devuelve los detalles de una Institucion"
    ),
    update=extend_schema(tags=["Instituciones"],
                         description="Actualiza una Institucion"),
    partial_update=extend_schema(
        tags=["Instituciones"], description="Actualiza una Institucion"
    ),
    destroy=extend_schema(tags=["Instituciones"],
                          description="Destruye una Institucion"),
    list=extend_schema(
        tags=["Instituciones"],
        description="Lista las Instituciones",
        parameters=[OpenApiParameter(name="query", required=False, type=str)],
    ),
)
class VistasDeInstituciones(
    usecases.CreateInstitucion,
    usecases.DetailInstitucion,
    usecases.DeleteInstitucion,
    usecases.ListInstitucion,
    usecases.UpdateInstitucion,
    viewsets.GenericViewSet,
):
    """Lee y actualiza los grupos."""

    queryset = InstitucionesManager().all()

    filter_backends = [filters.DjangoFilterBackend]

    filterset_fields = ["name"]

    # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get_serializer_class(self):
        return SerializadorDeInstituciones
