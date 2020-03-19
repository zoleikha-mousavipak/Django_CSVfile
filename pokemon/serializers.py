from rest_framework import serializers
from .models import Pokemon


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['Name', 'Type1', 'Type2', 'Total', 'HP', 'Attack', 'Defense', 'SpAtk', 'SpDef', 'Speed', 'Generation']
