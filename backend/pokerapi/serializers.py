from rest_framework import serializers
from .models import Game, Player

class PlayerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Player
		fields = ("name", "money", "pot_money")



class GameSerializer(serializers.ModelSerializer):
	players = PlayerSerializer(many=True, read_only=True)

	class Meta:
		model = Game
		fields = ("pk", "name", "small_blind", "big_blind", "pot", "players")
