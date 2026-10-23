from django.core.exceptions import ValidationError
from django.db import models

class Game(models.Model):
    class GameStatus(models.TextChoices):
        UPCOMING = 'UP', 'Upcoming'
        FINISHED = 'F', 'Finished'

    host_team = models.ForeignKey('teams.Team', on_delete=models.CASCADE, related_name='games_as_host')
    guest_team = models.ForeignKey('teams.Team', on_delete=models.CASCADE, related_name='games_as_guest')
    location = models.CharField(max_length=100)
    date_and_time = models.DateTimeField() #TODO: display it in a readable format.
    referee = models.CharField(max_length=100)
    status = models.CharField(max_length=2, choices=GameStatus)
    goals_host = models.PositiveIntegerField(default=0)
    goals_guest = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=~models.Q(
                    host_team=models.F('guest_team')
                ),
                name='different_host_and_guest_teams',
            ),
        ]

    def clean(self):
        super().clean()
        if self.host_team_id is not None and self.guest_team_id is not None and self.host_team_id == self.guest_team_id:
            raise ValidationError("A team cannot play against itself.")

    def __str__(self):
        return f'{self.host_team} - {self.guest_team}'

