from django.contrib import admin

from football.models import (
    Country,
    Player,
    TeamPlayers,
    Keeper,
) 

admin.site.register(Country)
admin.site.register(Player)
admin.site.register(TeamPlayers)
admin.site.register(Keeper)
