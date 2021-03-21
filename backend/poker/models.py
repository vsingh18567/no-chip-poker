from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models import CASCADE, SET_DEFAULT


class Player(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, blank=True)
    friends = models.ManyToManyField("self")


class FriendGroup(models.Model):
    date_created = models.DateField(auto_created=True)
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(Player, on_delete=CASCADE, related_name="groups_owned")
    players = models.ManyToManyField(Player, related_name="friend_groups")


class GamePlayer(models.Model):
    player = models.ForeignKey(Player, on_delete=CASCADE)
    money = models.PositiveIntegerField()
    is_busted = models.BooleanField()
    current_bid = models.PositiveIntegerField()


class Game(models.Model):
    time_created = models.DateTimeField(auto_created=True)
    name = models.CharField(max_length=6)
    owner = models.ForeignKey(Player, on_delete=CASCADE, related_name="games_owned")
    players = models.ManyToManyField(GamePlayer, related_name="games_played")
    friend_group = models.ForeignKey(
        FriendGroup, on_delete=SET_DEFAULT, default=None, related_name="games"
    )
    small_blind = models.PositiveIntegerField()
    big_blind = models.PositiveIntegerField()
    pot = models.PositiveIntegerField()
    current_player = models.ForeignKey(Player, on_delete=SET_DEFAULT, default=None, related_name="games_current_player")
