from rest_framework import serializers
from .models import Game, Player

# class GameNameSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Game
#         fields = ("name")

class PlayerSerializer(serializers.ModelSerializer):
    # game = GameNameSerializer(many=True, read_only=True)
    class Meta:
        model = Player
        fields = ("id", "name", "money", "pot_money", "status")


class GameSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = [
            "name",
            "small_blind",
            "big_blind",
            "pot",
            "players",
            "starting_money",
        ]
