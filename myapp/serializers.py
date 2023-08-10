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

class FileScoreSerializer(serializers.ModelSerializer):
    score = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    file_url = serializers.SerializerMethodField()
    
    class Meta:
        model = FileData
        fields = ('name', 'file_url', 'score',)
    
    def get_score(self, obj):
        # Get the score field name from the URL parameter
        score_field = self.context.get('score_field')
        
        # Retrieve the value of the specified score field from the model instance
        return getattr(obj, score_field, 0)  # Default to 0 if the score field doesn't exist
    
    def get_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    
    def get_file_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.file.url)

