from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    roles = serializers.StringRelatedField(many=True)
    nombre_completo = serializers.SerializerMethodField('get_nombre_completo')

    def get_nombre_completo(self, model):
        if model.first_name == model.last_name:
            return model.first_name
        return f'{model.last_name} {model.first_name}'

    class Meta:
        model = User
        fields = ('id', 'nombre_completo', 'username', 'email',
                  'roles', 'first_name', 'last_name', 'is_active')


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'


class BookmarkSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(many=False)

    class Meta:
        model = Bookmark
        fields = ('id', 'title', 'url', 'created_at', 'created_by')
