# from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

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
        context = super().get_context_data(**kwargs)
        context['page_title'] = f"{self.object.name} | SoftUni Cup"
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
    success_url = reverse_lazy('teams:list')