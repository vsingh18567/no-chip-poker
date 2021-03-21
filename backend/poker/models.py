from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Player(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	friends = models.ManyToManyField('self')

class FriendGroup(models.Model):
	date_created = models.DateField(auto_created=True)
	name = models.CharField(max_length=200)
	owner = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="groups_owned")
	players = models.ManyToManyField(Player, related_name="friend_groups")

class Game(models.Model):
	time_created = models.DateTimeField(auto_created=True)
	name = models.CharField(max_length=6)
	players = models.ManyToManyField(Player)
	friend_group = models.ForeignKey(FriendGroup, on_delete=models.SET_DEFAULT, default=None, related_name="games")


