# from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from games.models import Game
from teams.forms import TeamAddForm, TeamUpdateForm
from teams.models import Team


class AddTeamView(CreateView):
    template_name = 'teams/add_team.html'
    extra_context = {'page_title': 'Register a Team | SoftUni Cup'}
    model = Team
    form_class = TeamAddForm
    # success_url = reverse_lazy('teams:list')

    def get_success_url(self):
        return reverse('teams:details', kwargs={'slug': self.object.slug})

class TeamListView(ListView):
    template_name = 'teams/team_list.html'
    extra_context = {'page_title': 'Teams | SoftUni Cup'}
    model = Team
    context_object_name = 'teams'
    ordering = 'name'
    # paginate_by = 6

class TeamDetailsView(DetailView):
    template_name = 'teams/team_details.html'
    context_object_name = 'team'
    model = Team

    def get_context_data(self, **kwargs):
        current_points = 0

        finished_games_as_host = Game.objects.filter(host_team=self.object, status='F')
        for game in finished_games_as_host:
            if game.goals_host > game.goals_guest:
                current_points += 3
            elif game.goals_guest == game.goals_host:
                current_points += 1

        finished_games_as_guest = Game.objects.filter(guest_team=self.object, status='F')
        for game in finished_games_as_guest:
            if game.goals_host < game.goals_guest:
                current_points += 3
            elif game.goals_guest == game.goals_host:
                current_points += 1

        context = super().get_context_data(**kwargs)
        context['page_title'] = f"{self.object.name} | SoftUni Cup"
        context['current_points'] = current_points
        context['upcoming_games'] = Game.objects.filter(status='UP', host_team=self.object) | Game.objects.filter(status='UP', guest_team=self.object)
        context['finished_games'] = Game.objects.filter(status='F', host_team=self.object) | Game.objects.filter(status='F', guest_team=self.object)
        context['players'] = self.object.players.order_by('shirt_number')
        return context

class TeamUpdateView(UpdateView):
    template_name = 'teams/update_team.html'
    model = Team
    form_class = TeamUpdateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f"Update {self.object.name} | SoftUni Cup"
        return context

    def get_success_url(self):
        return reverse('teams:details', kwargs={'slug': self.object.slug})

class TeamDeleteView(DeleteView):
    template_name = 'teams/delete_team.html'
    extra_context = {'page_title': 'Delete Team | SoftUni Cup'}
    model = Team
    context_object_name = 'team'
    success_url = reverse_lazy('teams:list')