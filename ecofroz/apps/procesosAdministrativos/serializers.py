from rest_framework import serializers

from .models import RutaTransporte 

class SectoresSerializer2(serializers.ModelSerializer):
    
    class Meta:
        model = RutaTransporte
        fields = ('__all__')