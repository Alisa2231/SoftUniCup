from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from players.models import Player


class PlayerAddView(CreateView):
    model = Player
    template_name = 'players/add_player.html'

class PlayerUpdateView(UpdateView):
    model = Player
    template_name = 'players/update_player.html'

class PlayerDeleteView(DeleteView):
    model = Player
    template_name = 'players/delete_player.html'

class PlayerDetailsView(DetailView):
    model = Player
    template_name = 'players/player_details.html'