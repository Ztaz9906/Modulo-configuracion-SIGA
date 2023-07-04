from rest_framework import serializers
from .models import *
from django.contrib.auth.models import Group, Permission
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


class PermisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    permissions = PermisionSerializer()

    class Meta:
        model = Group
        fields = ['id', 'permissions', 'name']


class CustomLoginSerializer(LoginSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('email')
