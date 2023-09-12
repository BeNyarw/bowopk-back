from rest_framework import serializers
from api.models import Pokdx

class PokdxSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pokdx
        fields = '__all__'