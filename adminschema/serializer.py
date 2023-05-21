from rest_framework import serializers
from .models import *
from base.serializers import TbDpersonaSerializer
from django.contrib.auth import authenticate

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
    avatar = TbAvatarSerializer(read_only=True)
    password = serializers.CharField(write_only=True)
    id_persona = TbDpersonaSerializer(read_only=True)
    
    class Meta:
        model = TbUser
        fields = '__all__'

class TbUserCreateSerializer(serializers.ModelSerializer):
    # Añadimos un campo adicional para confirmar la contraseña
    password_confirm = serializers.CharField(write_only=True)
    class Meta:
        model = TbUser
        fields = ('username', 'password', 'password_confirm', 'email', 'id_institucion')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        # Validamos que los campos de contraseña coincidan
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Las contraseñas no coinciden.")
        return data
    def create(self, validated_data):
        # Eliminamos el campo de confirmación de la contraseña
        validated_data.pop('password_confirm')
        password = validated_data.pop('password')
        user = TbUser(**validated_data)
        user.set_password(password)
        user.save()
        return user