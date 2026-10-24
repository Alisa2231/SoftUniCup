from django import forms

from games.models import Game


class UpcomingGameBaseForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['host_team', 'guest_team', 'location', 'date_and_time', 'referee']
        labels = {
            'host_team': 'Host Team',
            'guest_team': 'Guest Team',
            'location': 'Location',
            'date_and_time': 'Date and Time',
            'referee': 'Referee',
        }
        widgets = {
            'location': forms.TextInput(attrs={'placeholder': 'Enter match location'}),
            'referee': forms.TextInput(attrs={'placeholder': 'Referee full name'}),
        }

class UpcomingGameAddForm(UpcomingGameBaseForm):
    ...

class UpcomingGameUpdateForm(UpcomingGameBaseForm):
    ...

class FinishedGameBaseForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['goals_host', 'goals_guest']
        labels = {
            'goals_host': 'Goals Host',
            'goals_guest': 'Goals Guest',
        }
        widgets = {
            'goals_host': forms.TextInput(attrs={'required': True}),
            'goals_guest': forms.TextInput(attrs={'required': True}),
        }

class FinishedGameForm(FinishedGameBaseForm):
    ...

class FinishedGameUpdateForm(FinishedGameBaseForm):
    ...