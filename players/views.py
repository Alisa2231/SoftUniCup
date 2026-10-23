from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from players.forms import PlayerAddForm, PlayerUpdateForm
from players.models import Player
from teams.models import Team


def player_add_view(request, team_slug):
    team = get_object_or_404(Team, slug=team_slug)

    if request.method == 'POST':
        form = PlayerAddForm(request.POST, request.FILES, team=team)
        if form.is_valid():
            player = form.save(commit=False)
            player.team = team
            player.save()
            return redirect('teams:details', slug=team_slug)
    else:
        form = PlayerAddForm(team=team)

    context = {'form': form, 'team': team, 'page_title': f'Add Player to {team.name}'}
    return render(request, 'players/add_player.html', context)

def player_edit_view(request, team_slug, pk):
    team = get_object_or_404(Team, slug=team_slug)
    player = get_object_or_404(Player, team=team, pk=pk)
    if request.method == 'POST':
        form = PlayerUpdateForm(request.POST, request.FILES, instance=player, team=team)
        if form.is_valid():
            form.save()
            return redirect('players:details', team_slug=team_slug, pk=pk)
    else:
        form = PlayerUpdateForm(instance=player, team=team)

    context = {'form': form, 'team': team, 'player': player, 'page_title': f'Edit Player of {team.name}'}
    return render(request, 'players/update_player.html', context)

def player_delete_view(request, team_slug, pk):
    team = get_object_or_404(Team, slug=team_slug)
    player = get_object_or_404(Player, team=team, pk=pk)
    if request.method == 'POST':
        player.delete()
        return redirect('teams:details', slug=team_slug)

    context = {'team': team, 'player': player, 'page_title': f'Delete Player of {team.name}'}
    return render(request, 'players/delete_player.html', context)

class PlayerDetailsView(DetailView):
    model = Player
    template_name = 'players/player_details.html'