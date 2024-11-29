from rest_framework import serializers
from users.models import Professor, UserProfileExample

class UserProfileExampleSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfileExample
        fields = ['id', 'address', 'phone_number', 'birth_date', 'user']


class ProfessorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Professor
        fields = "__all__"

class ProfessorCreateSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=140)
    matricula = serializers.CharField(max_length=12)
    departamento = serializers.CharField(max_length=140)
    login = serializers.CharField(max_length=100)
    senha = serializers.CharField(max_length=100)
