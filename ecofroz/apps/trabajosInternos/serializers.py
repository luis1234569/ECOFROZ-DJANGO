from rest_framework import serializers

from apps.activos.models import activo_areas 

class SectoresSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = activo_areas
        fields = ('__all__')

