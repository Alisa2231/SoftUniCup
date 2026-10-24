from django.shortcuts import render, redirect, get_object_or_404

from games.forms import UpcomingGameAddForm, UpcomingGameUpdateForm, FinishedGameForm, FinishedGameUpdateForm
from games.models import Game


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

    context = {'form': form}
    return render(request, 'games/add_game.html', context)

def game_update_view(request, slug):
    game = get_object_or_404(Game, slug=slug)
    if request.method == 'POST':
        form = UpcomingGameUpdateForm(request.POST, instance=game)
        if form.is_valid()and game.status == 'UP':
            form.save()
            return redirect('games:details', slug=slug)
    else:
        form = UpcomingGameUpdateForm(instance=game)

    context = {'form': form, 'game': game, 'page_title': 'Game Update | SoftUni Cup'}
    return render(request, 'games/update_game.html', context)

def game_finish_view(request, slug):
    game = get_object_or_404(Game, slug=slug)
    if request.method == 'POST':
        form = FinishedGameForm(request.POST, instance=game)
        if form.is_valid() and game.status == 'UP':
            game = form.save(commit=False)
            game.status = 'F'
            game.save()
            return redirect('games:details', slug=slug)
    else:
        form = FinishedGameForm(instance=game)

    context = {'form': form, 'game': game, 'page_title': 'Finished Game | SoftUni Cup'}
    return render(request, 'games/finish_game.html', context)

def correct_result_view(request, slug):
    game = get_object_or_404(Game, slug=slug)
    if request.method == 'POST':
        form = FinishedGameUpdateForm(request.POST, instance=game)
        if form.is_valid() and game.status == 'F':
            form.save()
            return redirect('games:details', slug=slug)
    else:
        form = FinishedGameForm(instance=game)

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
    game = get_object_or_404(Game, slug=slug)
    context = {'game': game, 'page_title': 'Game Details | SoftUni Cup'}
    return render(request, 'games/game_details.html', context)