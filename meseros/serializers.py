from rest_framework import serializers

from meseros.models import Meseros

class MeserosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meseros
        fields = ('nombre', 'edad')