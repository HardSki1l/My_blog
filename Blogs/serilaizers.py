# ma`lumotlarni tarjima qilib beradi python dan json ga json dan python ga
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from .models import UserModelBlog, TaskList


class UserSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = UserModelBlog


class DeleterSerializer(Serializer):
    username = serializers.CharField(max_length=10)

    # username = serializers.CharField(max_length=32)
    # password = serializers.CharField(max_length=16)


class UpdaterSerializer(Serializer):
    username = serializers.CharField(max_length=32)
    password = serializers.CharField(max_length=32)
    new_password = serializers.CharField(max_length=32)


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskList
        fields = ['date', 'comment', 'who']


class TaskFinder(serializers.ModelSerializer):
    class Meta:
        model = TaskList
        fields = ('comment',)

class CommentUpdateSerializer(serializers.Serializer):
    comment_id = serializers.IntegerField()
    comment = serializers.CharField(max_length=255)

class TaskSerializer(Serializer):
    task_id = serializers.IntegerField()
    user_id = serializers.IntegerField()
