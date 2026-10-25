from django.db.models import Model
from django.shortcuts import render, redirect, get_object_or_404

from games.forms import UpcomingGameAddForm, UpcomingGameUpdateForm, FinishedGameForm, FinishedGameUpdateForm
from games.models import Game
from teams.models import Team


def games_list_view(request):
    upcoming_games = Game.objects.filter(status='UP').select_related('host_team', 'guest_team').order_by('date_and_time')
    finished_games = Game.objects.filter(status='F').select_related('host_team', 'guest_team').order_by('date_and_time')
    context = {
        'page_title': 'Games | SoftUni Cup',
        'upcoming_games': upcoming_games,
        'finished_games': finished_games,
    }
    return render(request, 'games/game_list.html', context)

def game_add_view(request):
    if request.method == 'POST':
        form = UpcomingGameAddForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.status = 'UP'
            game.save()
            return redirect('games:list')
    else:
        form = UpcomingGameAddForm()

    context = {'form': form, 'page_title': 'Add Game | SoftUni Cup'}
    return render(request, 'games/add_game.html', context)

def game_update_view(request, slug):
    game = get_object_or_404(Game, slug=slug, status='UP')
    if request.method == 'POST':
        form = UpcomingGameUpdateForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('games:details', slug=slug)
    else:
        form = UpcomingGameUpdateForm(instance=game)

    context = {'form': form, 'game': game, 'page_title': 'Update Game | SoftUni Cup'}
    return render(request, 'games/update_game.html', context)

def game_finish_view(request, slug):
    game = get_object_or_404(Game, slug=slug, status='UP')
    if request.method == 'POST':
        game.status = 'F'
        form = FinishedGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('games:details', slug=slug)
    else:
        form = FinishedGameForm(instance=game)

    context = {'form': form, 'game': game, 'page_title': 'Finished Game | SoftUni Cup'}
    return render(request, 'games/finish_game.html', context)

def correct_result_view(request, slug):
    game = get_object_or_404(Game, slug=slug, status='F')
    if request.method == 'POST':
        form = FinishedGameUpdateForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('games:details', slug=slug)
    else:
        form = FinishedGameUpdateForm(instance=game)

    context = {'form': form, 'game': game, 'page_title': 'Update Finished Game | SoftUni Cup'}
    return render(request, 'games/correct_result.html', context)

def game_delete_view(request, slug):
    game = get_object_or_404(Game, slug=slug)
    if request.method == 'POST':
        game.delete()
        return redirect('games:list')

    context = {'game': game, 'page_title': 'Delete Game | SoftUni Cup'}
    return render(request, 'games/delete_game.html', context)

def game_details_view(request, slug):
    game = get_object_or_404(Game.objects.select_related('host_team', 'guest_team'), slug=slug)
    context = {'game': game, 'page_title': 'Game Details | SoftUni Cup'}
    return render(request, 'games/game_details.html', context)

def standings_view(request):
    teams = Team.objects.all()
    unsorted_results = {}
    for team in teams:
        unsorted_results[team.id] = {
            'team': team,
            "games_played": 0,
            "games_won": 0,
            "games_drawn": 0,
            "games_lost": 0,
            "goals_scored": 0,
            "goals_received": 0,
            'goal_difference': 0,
            "points": 0,
        }

    finished_games = Game.objects.filter(status='F')

    for game in finished_games:
        host = unsorted_results[game.host_team.id]
        guest = unsorted_results[game.guest_team.id]
        host['games_played'] += 1
        guest['games_played'] += 1
        if game.goals_host > game.goals_guest:
            host['games_won'] += 1
            host['points'] += 3
            guest['games_lost'] += 1
        elif game.goals_host < game.goals_guest:
            guest['games_won'] += 1
            guest['points'] += 3
            host['games_lost'] += 1
        else:
            host['games_drawn'] += 1
            host['points'] += 1
            guest['games_drawn'] += 1
            guest['points'] += 1
        host['goals_scored'] += game.goals_host
        host['goals_received'] += game.goals_guest
        guest['goals_scored'] += game.goals_guest
        guest['goals_received'] += game.goals_host

    for team_stats in unsorted_results.values():
        team_stats['goal_difference'] = team_stats['goals_scored'] - team_stats['goals_received']

    results = sorted(unsorted_results.values(), key=lambda x: (-x['points'], -x['goal_difference']))
    context = {'page_title': 'Standings | SoftUni Cup', 'results': results}
    return render(request, 'games/standings.html', context)