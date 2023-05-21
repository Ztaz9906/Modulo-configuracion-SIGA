from rest_framework import mixins,viewsets
from rest_framework.response import Response
from .models import TbUser, TbInstitucion
from .serializer import TbInstitucionSerializer
from rest_framework import status
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.registration.serializers import RegisterSerializer
################ Nuevo modelo #################################
class TbInstitucionViewSet(viewsets.ModelViewSet):
    queryset = TbInstitucion.objects.all()
    serializer_class = TbInstitucionSerializer
################   final     ################################
class CustomRegisterView(RegisterView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save(self.request)
        return Response(self.get_response_data(user))

    def get_response_data(self, user):
        return {'detail': 'Usuario registrado con éxito.'}

