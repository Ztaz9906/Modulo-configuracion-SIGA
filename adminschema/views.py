from rest_framework import viewsets, filters
from .models import TbUser, TbInstitucion
from .serializer import TbInstitucionSerializer, TbUserSerializer, GroupSerializer, CustomLoginSerializer
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


class CustomLoginView(LoginView):
    def get_serializer_class(self):
        return CustomLoginSerializer
