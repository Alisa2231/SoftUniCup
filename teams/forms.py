from django import forms

from teams.models import Team


class TeamBaseForm(forms.ModelForm):
    field_order = ['name', 'city', 'established_year', 'coach_name', 'coach_email','coach_phone_number', 'coach_image', 'logo']
    class Meta:
        model = Team
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name of your team', 'class': 'form-control'}),
            'city': forms.TextInput(attrs={'placeholder': 'City of the team', 'class': 'form-control'}),
            'established_year': forms.NumberInput(attrs={'placeholder': 'Year of establishment', 'class': 'form-control'}),
            'coach_name': forms.TextInput(attrs={'placeholder': 'Coach first and last name', 'class': 'form-control'}),
            'coach_email': forms.EmailInput(attrs={'placeholder': 'Coach email address', 'class': 'form-control'}),
            'coach_phone_number': forms.TextInput(attrs={'placeholder': 'Coach phone number', 'class': 'form-control'}),
            'coach_image': forms.FileInput(attrs={'class': 'form-control'}),
            'logo': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Team Name',
            'city': 'Team City',
            'logo': 'Team Logo',
            'established_year': 'Est. Year',
            'coach_name': 'Coach name',
            'coach_email': 'Coach email',
            'coach_phone_number': 'Coach phone number',
            'coach_image': 'Coach image',
        }

        error_messages = {
            'name': {'required': 'Team Name is a required field.'},
            'city': {'required': 'Team City is a required field.'},
            'coach_name': {'required': 'The name of the coach is required.'},
        }

class TeamAddForm(TeamBaseForm):
    ...

class TeamUpdateForm(TeamBaseForm):
    ...