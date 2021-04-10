from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Game
from .serializers import GameSerializer
from .utils import generate_name

class GameViewSet(viewsets.ModelViewSet):
	queryset = Game.objects.all()
	serializer_class = GameSerializer

	@action(methods=['post'], detail=False, url_name="create", url_path="create")
	def create_game(self, request):
		print("hi")
		name = generate_name()
		g = Game(
			name=name
		)
		g.save()
		return Response({"status": f"Game {name} created"})

