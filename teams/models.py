from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from teams.validators import up_to_current_year


class Team(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='teams/logos/', null=True, blank=True)
    established_year = models.PositiveIntegerField(validators=[MinValueValidator(1860), up_to_current_year], null=True, blank=True)
    coach_name = models.CharField(max_length=100)
    coach_email = models.EmailField(null=True, blank=True)
    coach_phone_number = models.CharField(null=True, blank=True)
    coach_image = models.ImageField(upload_to='teams/coaches/', null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, editable=False)
    # points = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'city'],
                name='unique_team_name_in_city'
            )
        ]

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.name}-{self.city}')
        super().save(*args, **kwargs)

    def __str__(self):
        if self.city in self.name:
            return self.name
        return f'{self.name} {self.city}'