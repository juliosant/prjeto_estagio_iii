from dataclasses import field
from pyexpat import model
from rest_framework.serializers import ModelSerializer
from .models import AgendamentoDoacao

# formulario
class AgendamentoDoacaoSerializer(ModelSerializer):
    class Meta:
        model = AgendamentoDoacao
        fields = '__all__'