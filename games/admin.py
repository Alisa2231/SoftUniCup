from django.contrib import admin

from games.models import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['host_team', 'guest_team', 'date_and_time', 'status']