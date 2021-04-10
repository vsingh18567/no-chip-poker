from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models import CASCADE, SET_DEFAULT

class Player(models.Model):
    name = models.CharField(max_length=40, null=False)
    money = models.PositiveIntegerField(default=0)
    pot_money = models.PositiveIntegerField(default=0)

class Game(models.Model):
    time_created = models.DateTimeField(auto_now_add=True, blank=True)
    players = models.ManyToManyField(Player, related_name="games_played")
    name = models.CharField(max_length=7, null=False, unique=True)
    small_blind = models.PositiveIntegerField(default=0)
    big_blind = models.PositiveIntegerField(default=0)
    pot = models.PositiveIntegerField(default=0)
    current_player = models.ForeignKey(Player, on_delete=SET_DEFAULT, default=None, null=True,
                                       related_name="games_current_player")


