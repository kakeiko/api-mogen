from rest_framework import serializers
from .models import Extrato

class ExtratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extrato
        fields = ['nome','valor','dia','ganho_gasto','dono']