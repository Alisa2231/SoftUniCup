from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.text import slugify


class Team(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='teams/logos/', null=True, blank=True)
    established_year = models.PositiveIntegerField(validators=[MinValueValidator(1860), MaxValueValidator(2026)], null=True, blank=True)
    coach_name = models.CharField(max_length=100)
    coach_email = models.EmailField(null=True, blank=True)
    coach_phone_number = models.PositiveIntegerField(null=True, blank=True)
    coach_image = models.ImageField(upload_to='teams/coaches/', null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, editable=False)
    points = models.PositiveIntegerField(default=0)
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
        return self.name