from rest_framework import serializers
from .models import *
from base.serializers import TbDpersonaSerializer

class TbAvatarSerializer(serializers.ModelSerializer):
   class Meta:
        model = TbUser
        fields = '__all__'

class TbUserCreateSerializer(serializers.ModelSerializer):
    
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
    
    