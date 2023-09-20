from rest_framework import viewsets
from .models import *
from .serializers import *


class TbTorpedoViewSet(viewsets.ModelViewSet):
    queryset = TbDpersonaTorpedo.objects.all()
    serializer_class = TbDpersonaTorpedoSerializer


class TbDpersonaViewSet(viewsets.ModelViewSet):
    queryset = TbDpersona.objects.all()
    serializer_class = TbDpersonaSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TbDpersonaSerializer
        else:
            return TbDpersonaCreateSerializer
