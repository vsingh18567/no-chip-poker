from rest_framework import viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response

from .models import Game
from .serializers import GameSerializer
from .utils import generate_name

@api_view(["GET"])
def games_list(request):
    games = Game.objects.all()
    return Response(GameSerializer(games, many=True).data, status=200)

@api_view(["GET"])
def games_detail(request, name):
    try:
        game = Game.objects.get(name=name)
        return Response(GameSerializer(game).data, status=200)
    except:
        return Response({"status": f"game with name {name} not found"}, status=400)


