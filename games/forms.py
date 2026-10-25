from django import forms

from games.models import Game


class UpcomingGameBaseForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['host_team', 'guest_team', 'location', 'date_and_time', 'referee']
        widgets = {
            'location': forms.TextInput(attrs={'placeholder': 'Enter match location'}),
            'date_and_time': forms.DateTimeInput(format='%Y-%m-%dT%H:%M', attrs={'type': 'datetime-local'}),
            'referee': forms.TextInput(attrs={'placeholder': 'Referee full name'}),
        }
        error_messages = {
            'host_team': {'required': 'Please choose the host team.'},
            'guest_team': {'required': 'Please choose the guest team.'},
            'location': {'required': 'Please enter the location of the match.'},
            'date_and_time': {'required': 'Please enter the timing of the match.'},
            'referee': {'required': "Please enter the referee's full name."},
        }

class UpcomingGameAddForm(UpcomingGameBaseForm):
    ...

class UpcomingGameUpdateForm(UpcomingGameBaseForm):
    class Meta(UpcomingGameBaseForm.Meta):
        fields = ['location', 'date_and_time', 'referee']

class FinishedGameBaseForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['goals_host', 'goals_guest']
        error_messages = {
            'goals_host': {'required': 'Please enter the number of goals the host team scored.'},
            'goals_guest': {'required': 'Please enter the number of goals the guest team scored.'}
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['goals_host'].required = True
        self.fields['goals_guest'].required = True

class FinishedGameForm(FinishedGameBaseForm):
    ...

class FinishedGameUpdateForm(FinishedGameBaseForm):
    ...