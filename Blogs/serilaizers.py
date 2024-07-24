# ma`lumotlarni tarjima qilib beradi python dan json ga json dan python ga
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from .models import UserModelBlog


class UserSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = UserModelBlog


class DeleterSerializer(Serializer):
    username = serializers.CharField(max_length=10)

    # username = serializers.CharField(max_length=32)
    # password = serializers.CharField(max_length=16)
