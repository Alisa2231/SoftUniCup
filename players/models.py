from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.text import slugify


class Player(models.Model):
    class Positions(models.TextChoices):
        GK = 'GK', "Goalkeeper"
        RB = 'RB', "Right Back"
        CB = 'CB', "Center Back"
        LB = 'LB', "Left Back"
        CDM ='CDM', "Center Defensive Midfielder"
        CM = 'CM', "Center Midfielder"
        CAM = 'CAM', "Center Attacking Midfielder"
        RM = 'RM', "Right Midfielder"
        LM = 'LM', "Left Midfielder"
        LW = 'LW', "Left Winger"
        RW = 'RW', "Right Winger"
        CF = 'CF', "Center Forward"
        ST = 'ST', "Striker"

    class PreferredFoot(models.TextChoices):
        RIGHT = 'R', "Right"
        LEFT = 'L', "Left"
        BOTH = 'B', "Both"

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100, null=True, blank=True)
    birth_date = models.DateField()
    shirt_number = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(99)])
    main_position = models.CharField(max_length=100, choices = Positions)
    secondary_position = models.CharField(max_length=100, choices = Positions, null=True, blank=True)
    preferred_foot = models.CharField(max_length=100, choices = PreferredFoot)
    height = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0)], null=True, blank=True)
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