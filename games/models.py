from django.core.exceptions import ValidationError
from django.db import models
from django.template.defaultfilters import slugify


class Game(models.Model):
    class GameStatus(models.TextChoices):
        UPCOMING = 'UP', 'Upcoming'
        FINISHED = 'F', 'Finished'

    host_team = models.ForeignKey('teams.Team', on_delete=models.CASCADE, related_name='games_as_host')
    guest_team = models.ForeignKey('teams.Team', on_delete=models.CASCADE, related_name='games_as_guest')
    location = models.CharField(max_length=100)
    date_and_time = models.DateTimeField() #TODO: display it in a readable format
    referee = models.CharField(max_length=100)
    status = models.CharField(max_length=2, choices=GameStatus, default=GameStatus.UPCOMING)
    goals_host = models.PositiveIntegerField(null=True, blank=True)
    goals_guest = models.PositiveIntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, unique=True, editable=False)

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=~models.Q(
                    host_team=models.F('guest_team')
                ),
                name='different_host_and_guest_teams',
            ),
            models.UniqueConstraint(
                fields=['host_team', 'guest_team'],
                name='unique_host_and_guest_teams',
            )
        ]

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.host_team.slug}-vs-{self.guest_team.slug}')
        super().save(*args, **kwargs)

    def clean(self):
        super().clean()
        if self.host_team_id is not None and self.guest_team_id is not None and self.host_team_id == self.guest_team_id:
            raise ValidationError("A team cannot play against itself.")

        if self.status == self.GameStatus.FINISHED:
            if self.goals_host is None or self.goals_guest is None:
                raise ValidationError("Both scores must be provided for a finished game. If a team didn't score a goal, just enter 0.")
        elif self.status == self.GameStatus.UPCOMING:
            if self.goals_host is not None or self.goals_guest is not None:
                raise ValidationError("Upcoming games cannot have a recorded score.")

    def __str__(self):
        return f'{self.host_team} vs {self.guest_team}'

