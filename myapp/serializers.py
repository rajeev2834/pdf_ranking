from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import CustomUser, FileData

class CustomUserCreateSerializer(UserCreateSerializer):

    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ('id', 'email', 'password', 'first_name', 'last_name')

class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name')

class FileDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileData
        fields = ('user','file_name', 'file',)

class FileDataCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileData
        fields = ('file_name', 'file')
