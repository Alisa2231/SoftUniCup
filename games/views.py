from django.shortcuts import render

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
    ...

def game_update_view(request, slug):
    ...

def game_finish_view(request, slug):
    ...

def correct_result_view(request, slug):
    ...

def game_delete_view(request, slug):
    ...

def game_details_view(request, slug):
    ...