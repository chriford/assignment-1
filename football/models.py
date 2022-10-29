from django.db import models


class Country(models.Model):
    name = models.CharField(
        max_length=100,
        null=True,
        blank=False,
    )
    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(
        max_length=100,
        null=True,
        blank=False,
    )
    jersey_number = models.IntegerField(
        null=True,
        blank=True,
    )
    country = models.ForeignKey(
        to=Country,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class TeamPlayers(models.Model):
    players = models.ManyToManyField(
        to=Player,
        null=True,
        blank=False,
    )
    
    def __str__(self):
        return self.players

