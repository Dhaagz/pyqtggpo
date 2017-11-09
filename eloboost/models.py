from django.db import models
from django.conf import settings

class Game(models.Model):
    title = models.CharField(max_length=64)
    short_title = models.CharField(max_length=32)

class Rank(models.Model):
    title = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

class Contract(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='client_of', null=True)
    booster = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='booster_of', null=True)
    game = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True)
    initial_rank = models.ForeignKey(Rank, on_delete=models.SET_NULL, related_name='initial_rank_of', null=True)
    wanted_rank = models.ForeignKey(Rank, on_delete=models.SET_NULL, related_name='wanted_rank_of', null=True)
    claim_date = models.DateTimeField(auto_now=False,auto_now_add=True)
    expiration_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
