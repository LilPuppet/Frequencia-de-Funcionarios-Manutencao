from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from users.api.serializers import ProfessorCreateSerializer, ProfessorSerializer, UserProfileExampleSerializer

from users.models import Professor, UserProfileExample

class UserProfileExampleViewSet(ModelViewSet):
    serializer_class = UserProfileExampleSerializer
    permission_classes = [AllowAny]
    queryset = UserProfileExample.objects.all()
    http_method_names = ['get', 'put']

class ProfessorViewSet(ModelViewSet):
    serializer_class = ProfessorSerializer
    permission_classes = [AllowAny]
    queryset = Professor.objects.all()

    def create(self, request):
        serializer = ProfessorCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        novo_user = User.objects.create_user(
            username=serializer.validated_data['login'],
            password=serializer.validated_data['senha'],
        )

        novo_professor = Professor.objects.create(
            nome=serializer.validated_data['nome'],
            matricula=serializer.validated_data['matricula'],
            departamento=serializer.validated_data['departamento'],
            user=novo_user
        )

        serializer_saida = ProfessorSerializer(novo_professor)
        return Response({"Info": "Cadastro realizado!", "data":serializer_saida.data}, status=status.HTTP_201_CREATED)