
# Junior Interview Questions

#### 1. what command is used to create a django project

#### 2. why is it neccessary to register your django models in the admin.py file

## Study the models below and answer the questions as follows:
```
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
        blank=False,
    )
    country = models.ForeignKey(
        to=Country,
        on_delete=models.CASCADE,
        null=True,
        blank=False,
    )
    is_striker = models.BooleanField(default=False)

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


class Keeper(models.Model):
    name = models.CharField(
        max_length=100,
        null=True,
        blank=False
    )
    jersey_number = models.IntegerField(
        null=True,
        blank=False,
    )
    country = models.ForeignKey(
        to=Country,
        on_delete=models.CASCADE,
        null=True,
        blank=False,
    )
    team = models.ForeignKey(
        to=TeamPlayers, 
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


```

#### 1. state the use of the __ str __ method on a django model
#### 2. on the model called **Player**, there is a field called country, what is the use of a ForeignKey.?

###### what is the use of an on_delete parameter on every ForeignKey field(e.g country).?

#### 3. what is the difference between the null and blank field parameters?

#### 4. on the model called TeamPlayers, there is a field called players, what is the use of a ManyToManyField?

#### 5. on most of the models, there is a CharField which has a parameter called max_length, what is the use of the parameter

## The End of assignment 1