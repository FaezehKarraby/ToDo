from django.contrib.auth.models import User
from rest_framework import serializers
from todo.models import TodoModel


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        exclude = ()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
