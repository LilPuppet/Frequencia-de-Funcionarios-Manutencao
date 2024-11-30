from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from users.api.serializers import FuncionarioCreateSerializer, FuncionarioSerializer, UserProfileExampleSerializer

from users.models import Funcionario, UserProfileExample

class UserProfileExampleViewSet(ModelViewSet):
    serializer_class = UserProfileExampleSerializer
    permission_classes = [AllowAny]
    queryset = UserProfileExample.objects.all()
    http_method_names = ['get', 'put']

class FuncionarioViewSet(ModelViewSet):
    serializer_class = FuncionarioSerializer
    permission_classes = [AllowAny]
    queryset = Funcionario.objects.all()

    def create(self, request):
        serializer = FuncionarioCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        novo_user = User.objects.create_user(
            username=serializer.validated_data['login'],
            password=serializer.validated_data['senha'],
        )

        novo_Funcionario = Funcionario.objects.create(
            nome=serializer.validated_data['nome'],
            matricula=serializer.validated_data['matricula'],
            departamento=serializer.validated_data['departamento'],
            user=novo_user
        )

        serializer_saida = FuncionarioSerializer(novo_Funcionario)
        return Response({"Info": "Cadastro realizado!", "data":serializer_saida.data}, status=status.HTTP_201_CREATED)