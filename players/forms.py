from django import forms

from players.models import Player


class PlayerBaseForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter first name', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter last name', 'class': 'form-control'}),
            'nationality': forms.TextInput(attrs={'placeholder': 'Enter nationality', 'class': 'form-control'}),
            'birth_year': forms.NumberInput(attrs={'placeholder': 'Enter year of birth', 'class': 'form-control'}),
            'shirt_number': forms.NumberInput(attrs={'placeholder': 'Enter shirt number', 'class': 'form-control'}),
            'main_position': forms.Select(attrs={'class': 'form-control'}),
            'secondary_position': forms.Select(attrs={'class': 'form-control'}),
            'preferred_foot': forms.Select(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'placeholder': 'Enter height in cm', 'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'first_name': "First Name",
            'last_name': "Last Name",
            'birth_year': "Birth Year",
            'shirt_number': "Shirt Number",
            'main_position': "Main Position",
            'secondary_position': "Secondary Position",
            'preferred_foot': "Preferred Foot",
            'height': "Height (cm)",
            'image': "Upload Image",
        }
        help_texts = {
            'shirt_number': 'Must be unique in the team',
        }
        error_messages = {
            'first_name': {'required': "Please enter player's first name"},
            'last_name': {'required': "Please enter player's last name"},
            'nationality': {'required': "Please enter player's nationality"},
            'birth_year': {'required': "Please enter player's year of birth"},
            'shirt_number': {'required': "Please enter player's shirt number"},
            'main_position': {'required': "Please enter player's main position"}
        }

    def __init__(self, *args, team=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.team = team

    def clean_shirt_number(self):
        shirt_number = self.cleaned_data['shirt_number']

        players = Player.objects.filter(
            team=self.team,
            shirt_number=shirt_number,
        )

        if self.instance.pk:
            players = players.exclude(pk=self.instance.pk)

        if players.exists():
            raise forms.ValidationError(
                'This shirt number is already taken by another player on this team.'
            )

        return shirt_number


class PlayerAddForm(PlayerBaseForm):
    ...

class PlayerUpdateForm(PlayerBaseForm):
    ...