from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import status
from users.api.serializers import FuncionarioCreateSerializer, FuncionarioSerializer, UserProfileExampleSerializer
from users.models import Funcionario, UserProfileExample

class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response({"error": "Credenciais inválidas!"}, status=status.HTTP_401_UNAUTHORIZED)

class FuncionarioView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, pk=None):
        if pk:
            try:
                funcionario = Funcionario.objects.get(pk=pk)
                serializer = FuncionarioSerializer(funcionario)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Funcionario.DoesNotExist:
                return Response({"error": "Funcionário não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        funcionarios = Funcionario.objects.all()
        serializer = FuncionarioSerializer(funcionarios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = FuncionarioCreateSerializer(data=request.data)
        if serializer.is_valid():
            funcionario = serializer.save()  # Chama o método `create` do serializer
            return Response(
                {"message": "Funcionário criado com sucesso!", "data": FuncionarioSerializer(funcionario).data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            funcionario = Funcionario.objects.get(pk=pk)
        except Funcionario.DoesNotExist:
            return Response({"error": "Funcionário não encontrado"}, status=status.HTTP_404_NOT_FOUND)

        serializer = FuncionarioCreateSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            if 'login' in serializer.validated_data:
                funcionario.user.username = serializer.validated_data['login']
                funcionario.user.save()

            funcionario.nome = serializer.validated_data.get('nome', funcionario.nome)
            funcionario.matricula = serializer.validated_data.get('matricula', funcionario.matricula)
            funcionario.departamento = serializer.validated_data.get('departamento', funcionario.departamento)
            funcionario.save()
            return Response(
                {"message": "Funcionário atualizado com sucesso!", "data": FuncionarioSerializer(funcionario).data},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            funcionario = Funcionario.objects.get(pk=pk)
            funcionario.user.delete()  # Exclui também o usuário vinculado
            funcionario.delete()
            return Response({"message": "Funcionário excluído com sucesso!"}, status=status.HTTP_204_NO_CONTENT)
        except Funcionario.DoesNotExist:
            return Response({"error": "Funcionário não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, pk=None):
        if pk:
            try:
                profile = UserProfileExample.objects.get(pk=pk)
                serializer = UserProfileExampleSerializer(profile)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except UserProfileExample.DoesNotExist:
                return Response({"error": "Perfil não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        else:
            profiles = UserProfileExample.objects.all()
            serializer = UserProfileExampleSerializer(profiles, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserProfileExampleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            profile = UserProfileExample.objects.get(pk=pk)
        except UserProfileExample.DoesNotExist:
            return Response({"error": "Perfil não encontrado"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserProfileExampleSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            profile = UserProfileExample.objects.get(pk=pk)
            profile.delete()
            return Response({"message": "Perfil excluído com sucesso"}, status=status.HTTP_204_NO_CONTENT)
        except UserProfileExample.DoesNotExist:
            return Response({"error": "Perfil não encontrado"}, status=status.HTTP_404_NOT_FOUND)