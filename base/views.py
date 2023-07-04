from rest_framework import viewsets
from .models import *
from .serializers import *


class TbTorpedoViewSet(viewsets.ModelViewSet):
    queryset = TbDpersonaTorpedo.objects.all()
    serializer_class = TbDpersonaTorpedoSerializer
