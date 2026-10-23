from django.urls import path, include

from players.views import PlayerDeleteView, PlayerDetailsView, player_add_view, player_edit_view

app_name = 'players'

urlpatterns = [
    path('<slug:team_slug>/', include([
        path('add/', player_add_view, name='add'),
        path('<int:pk>/', include([
            path('update/', player_edit_view, name='update'),
            path('delete/', PlayerDeleteView.as_view(), name='delete'),
            path('details/', PlayerDetailsView.as_view(), name='details'),
        ]))
    ]))
]