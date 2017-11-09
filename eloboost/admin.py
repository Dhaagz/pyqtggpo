from django.contrib import admin
from eloboost.models import Game,Rank

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
        pass

@admin.register(Rank)
class RankAdmin(admin.ModelAdmin):
        pass
