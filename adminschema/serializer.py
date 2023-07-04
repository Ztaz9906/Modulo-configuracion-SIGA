from rest_framework import serializers
from .models import *
from base.serializers import TbDpersonaSerializer
from dj_rest_auth.serializers import LoginSerializer
################ Nuevo modelo #################################


class TbInstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbInstitucion
        fields = '__all__'
################   final     #################################


class TbAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbUser
        fields = '__all__'


class TbUserSerializer(serializers.ModelSerializer):
    """SERIALIZA EL OBJETO DE PERFIL DE USUARIO"""
    class Meta:
        model = TbUser
        fields = ['username', 'email', 'password', 'rol', 'id_institucion']
        extra_kwargs = {
            'password': {
                "write_only": True,
                "style": {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Crear y retorna un nuevo usuario"""
        rol = validated_data.pop('rol')
        user = TbUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            id_institucion=validated_data['id_institucion'],
            password=validated_data["password"],
            rol=rol,
        )
        return user


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class CustomLoginSerializer(LoginSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('email')
