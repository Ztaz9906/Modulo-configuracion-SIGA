from rest_framework import mixins,viewsets,filters
from rest_framework.response import Response
from .models import TbUser, TbInstitucion,TbSystem
from .serializer import TbInstitucionSerializer,TbUserSerializer,GroupSerializer,TbSystemSerializer,CustomLoginSerializer
from rest_framework import status
from django.contrib.auth.models import Group
from dj_rest_auth.views import LoginView
################ Nuevo modelo #################################
class TbInstitucionViewSet(viewsets.ModelViewSet):
    queryset = TbInstitucion.objects.all()
    serializer_class = TbInstitucionSerializer
################   final     ################################
class TbUserViewSet(viewsets.ModelViewSet):
    """Genera el CRUD de los usuarios"""
    serializer_class = TbUserSerializer
    queryset = TbUser.objects.all()

    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'email')
    def get_response_data(self, user):
        return {'detail': 'Usuario registrado con éxito.'}

class GroupViewSet(viewsets.ModelViewSet):
    """"Genera CRUD de los GRUPOS de permisos"""
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

class TbSystemViewSet(viewsets.ModelViewSet):
    """"Genera CRUD de los GRUPOS de permisos"""
    serializer_class = TbSystemSerializer
    queryset = TbSystem.objects.all()
    
class CustomLoginView(LoginView):
    def get_serializer_class(self):
        return CustomLoginSerializer