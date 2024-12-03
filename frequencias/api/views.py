from datetime import datetime
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from frequencias.api.serializers import FrequenciaSerializer
from frequencias.models import FrequenciaModel
from users.api.serializers import FuncionarioSerializer

class FrequenciaViewSet(ModelViewSet):
    serializer_class = FrequenciaSerializer
    permission_classes = [IsAuthenticated]
    queryset = FrequenciaModel.objects.all()

    def create(self, request):
        serializer = FuncionarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        funcionario = serializer.validated_data['funcionario']
        hora_atual = datetime.now()

        frequencia_aberta = FrequenciaModel.objects.filter(funcionario=funcionario, hora_fim__isnull=True).exists()

        if frequencia_aberta:
            frequencia_aberta.hora_fim = hora_atual
            frequencia_aberta.save()
            serializer_saida = FrequenciaSerializer(frequencia_aberta)
            return Response(
                {"Info": "Frequência encerrada com sucesso!", "data": serializer_saida.data},
                status=status.HTTP_200_OK
            )
        else: #pegar o funcionario
            nova_frequencia = FrequenciaModel.objects.create(
                funcionario=funcionario,
                hora_inicio=hora_atual,
                hora_fim=None
            )
            serializer_saida = FrequenciaSerializer(nova_frequencia)
            return Response(
                {"Info": "Frequência iniciada com sucesso!", "data": serializer_saida.data},
                status=status.HTTP_201_CREATED
            )
