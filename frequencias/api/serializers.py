from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from frequencias.models import FrequenciaModel

class FrequenciaSerializer(ModelSerializer):

    class Meta:
        model = FrequenciaModel
        fields = "__all__"

class FrequenciaCreateSerializer(serializers.Serializer):
    
    funcionario = serializers.IntegerField()
    hora_inicio = serializers.DateTimeField()
    hora_fim = serializers.DateTimeField(required=False, default=None)
    