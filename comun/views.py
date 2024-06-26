from rest_framework import viewsets


# noinspection PyUnresolvedReferences
class ByOperationSerializer:
    def get_serializer_class(self: viewsets.GenericViewSet):
        old: dict = super().get_serializer_class()
        if self.action in old:
            return old.get(self.action)
        elif self.request.method in ["GET", "HEAD", "OPTIONS"]:
            return old.get("read")
        return old.get("write")


# noinspection PyUnresolvedReferences
class ByVersionSerializer:
    def get_serializer_class(self):
        old: dict = super().get_serializer_class()
        return old.get(self.request.version)
