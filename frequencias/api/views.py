from datetime import datetime
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from frequencias.api.serializers import FrequenciaSerializer
from frequencias.models import FrequenciaModel
from users.api.serializers import FuncionarioSerializer

class FrequenciaViewSet(ModelViewSet):
    serializer_class = FrequenciaSerializer
    permission_classes = [AllowAny]
    queryset = FrequenciaModel.objects.all()

    def create(self, request):
        serializer_func = FrequenciaSerializer(data=request.data)
        serializer_func.is_valid(raise_exception=True)
        funcionario = serializer_func.validated_data['funcionario']
        hora_atual = datetime.now()

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
    
    
    def partial_update(self, request, *args, **kwargs):
        frequencia = self.get_object()
        frequencia.hora_fim = datetime.now()
        frequencia.save()
        serializer_saida = FrequenciaSerializer(frequencia)
        return Response(
            {"Info": "Atualização realizada com sucesso!", "data": serializer_saida.data},
            status=status.HTTP_200_OK
        )
