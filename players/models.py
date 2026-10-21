from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.text import slugify


class Player(models.Model):
    class Positions(models.TextChoices):
        GOAL_KEEPER = 'GK', "Goal Keeper"
        #TODO: check with Pepi

    class PreferredFoot(models.TextChoices):
        RIGHT = 'R', "Right"
        LEFT = 'L', "Left"
        BOTH = 'B', "Both"

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    shirt_number = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(99)])
    main_position = models.CharField(max_length=100, choices = Positions)
    preferred_foot = models.CharField(max_length=100, choices = PreferredFoot)
    height = models.PositiveIntegerField(null=True, blank=True)
    # weight = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='players/', null=True, blank=True)
    # slug = models.SlugField(unique=True, editable=False)
    team = models.ForeignKey('teams.Team', on_delete=models.CASCADE, related_name='players', editable=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['shirt_number', 'team'],
                name='unique_shirt_number_in_team'
            )
        ]

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(f'{self.first_name}-{self.last_name}-{self.shirt_number}-{self.team}')
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'