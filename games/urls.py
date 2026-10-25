from django.urls import path, include

from games.views import games_list_view, game_add_view, game_update_view, game_finish_view, correct_result_view, \
    game_delete_view, game_details_view, standings_view

app_name = 'games'

urlpatterns = [
    path('', games_list_view, name='list'),
    path('add/', game_add_view, name='add'),
    path('<slug:slug>/', include([
        path('update/', game_update_view, name='update'),
        path('finish/', game_finish_view, name='finish'),
        path('correct-result/', correct_result_view, name='correct'),
        path('delete/', game_delete_view, name='delete'),
        path('details/', game_details_view, name='details'),
    ])),
    path('standings/', standings_view, name='standings'),
]