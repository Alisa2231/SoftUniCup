from django.urls import path, include

from teams.views import AddTeamView, TeamListView, TeamDetailsView, TeamUpdateView, TeamDeleteView

app_name = 'teams'
urlpatterns = [
    path('', TeamListView.as_view(), name='list'),
    path('add/', AddTeamView.as_view(), name='add'),
    path('<slug:slug>/', include([
        path('team-details/', TeamDetailsView.as_view(), name='details'),
        path('update/', TeamUpdateView.as_view(), name='update'),
        path('delete/', TeamDeleteView.as_view(), name='delete'),
    ]))
]