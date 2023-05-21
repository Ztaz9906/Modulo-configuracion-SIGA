from rest_framework import mixins,viewsets
from django.contrib.auth.models import User
from .serializer import TbUserCreateSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from .models import TbUser, TbInstitucion
from .serializer import TbInstitucionSerializer
from rest_framework import status
from django.contrib.auth.hashers import check_password, make_password
################ Nuevo modelo #################################
class TbInstitucionViewSet(viewsets.ModelViewSet):
    queryset = TbInstitucion.objects.all()
    serializer_class = TbInstitucionSerializer
################   final     ################################
