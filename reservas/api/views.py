from typing import Any
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from reservas.api.serializers import ReservaSerializer, SalaSerializer
from reservas.models import ReservaModel, SalaModel

class SalaViewSet(ModelViewSet):
    serializer_class = SalaSerializer
    permission_classes = [IsAdminUser]
    queryset = SalaModel.objects.all()

    def create(self, request):
        serializer = SalaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        numero = serializer.validated_data['numero']
        bloco = serializer.validated_data['bloco']

        in_database = SalaModel.objects.filter(numero=numero, bloco=bloco).exists()

        if not in_database:
            nova_sala = SalaModel.objects.create(
                numero=serializer.validated_data['numero'],
                bloco=serializer.validated_data['bloco'],
                capacidade=serializer.validated_data['capacidade'],
                tipo=serializer.validated_data['tipo'],
                disponivel=serializer.validated_data['disponivel']
            )

            serializer_saida = SalaSerializer(nova_sala)

            return Response({"Info": "Sala criada!", "data": serializer_saida.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"Info": "Falha ao tentar cadastrar a sala!"}, status=status.HTTP_409_CONFLICT)

class ReservaViewSet(ModelViewSet):
    serializer_class = ReservaSerializer
    permission_classes = [IsAuthenticated]
    queryset = ReservaModel.objects.all()
    
    def create(self, request):
        serializer = ReservaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        sala_numero = serializer.validated_data['sala_numero']
        hora_inicio = serializer.validated_data['hora_inicio']
        hora_fim = serializer.validated_data['hora_fim']

        sala_existe = SalaModel.objects.filter(numero=sala_numero).exists()
        in_conflict = ReservaModel.objects.filter(sala_numero=sala_numero, hora_inicio__lt=hora_fim, hora_fim__gt=hora_inicio).exists()

        if sala_existe and not in_conflict:
            nova_reserva = ReservaModel.objects.create(
                sala_numero=serializer.validated_data['sala_numero'],
                hora_inicio=serializer.validated_data['hora_inicio'],
                hora_fim=serializer.validated_data['hora_fim']
            )

            serializer_saida = ReservaSerializer(nova_reserva)
            return Response({"Info": "Reserva cadastrada!", "data":serializer_saida.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"Info": "Falha ao tentar cadastrar reserva!"},status=status.HTTP_409_CONFLICT)