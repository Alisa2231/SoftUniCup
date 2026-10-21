from django.db import models

class Game(models.Model):
    class GameStatus(models.TextChoices):
        UPCOMING = 'UP', 'Upcoming'
        FINISHED = 'F', 'Finished'

    host_team = models.ForeignKey('teams.Team', on_delete=models.CASCADE, related_name='games_as_host')
    guest_team = models.ForeignKey('teams.Team', on_delete=models.CASCADE, related_name='games_as_guest')
    location = models.CharField(max_length=100) #add locations model and make the field foreignkey?
    date_and_time = models.DateTimeField()
    status = models.CharField(max_length=100, choices=GameStatus)
    goals_host = models.PositiveIntegerField(default=0)
    goals_guest = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.host_team} - {self.guest_team}'

    #TODO: verify host team is not the same as guest team!

