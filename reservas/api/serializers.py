from rest_framework.serializers import ModelSerializer

from reservas.models import ReservaModel, SalaModel

class SalaSerializer(ModelSerializer):

    class Meta:
        model = SalaModel
        fields = "__all__"

class ReservaSerializer(ModelSerializer):

    class Meta:
        model = ReservaModel
        fields = "__all__"
