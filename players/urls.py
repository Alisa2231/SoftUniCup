from django.urls import path, include

from players.views import PlayerAddView, PlayerUpdateView, PlayerDeleteView, PlayerDetailsView

app_name = 'players'

urlpatterns = [
    path('<slug:team_slug>/', include([
        path('add/', PlayerAddView.as_view(), name='add'),
        path('<int:pk>/', include([
            path('update/', PlayerUpdateView.as_view(), name='update'),
            path('delete/', PlayerDeleteView.as_view(), name='delete'),
            path('details/', PlayerDetailsView.as_view(), name='details'),
        ]))
    ]))
]