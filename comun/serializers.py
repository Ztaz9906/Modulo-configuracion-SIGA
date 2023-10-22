import importlib
import logging
from abc import abstractmethod

from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer
from drf_spectacular.utils import extend_schema_field, OpenApiTypes
from rest_framework_recursive.fields import RecursiveField as RFRecursiveField

RecursiveField = extend_schema_field(OpenApiTypes.OBJECT)(RFRecursiveField)


def polymorphic(model, *_serializers):
    final_klass_name = f"{model.__class__.__name__}PolymorphicSerializer"
    logger = logging.getLogger(final_klass_name)
    classes = []
    for imp in _serializers:
        split = str.split(imp, ".")
        package = ".".join(split[:-1])
        try:
            classes.append(getattr(importlib.import_module(package), split[-1]))
        except Exception as e:
            logger.warning(str(e))
    return type(
        final_klass_name,
        (PolymorphicSerializer,),
        {
            "resource_type_field_name": "resourcetype",
            "model_serializer_mapping": {
                k.Meta.model: k for k in classes  # type: ignore
            },
        },
    )


class BorrableLectura(serializers.HyperlinkedModelSerializer):
    """Usado para marcar un objeto serializable como borrable."""

    borrable = serializers.SerializerMethodField("get_borrable", read_only=True)

    @abstractmethod
    def get_borrable(self, obj) -> bool:
        """Retorna si un objeto es borrable (True) o no (False)."""
        raise NotImplementedError()

    class Meta:
        fields = ["borrable"]
