from django.core.exceptions import ValidationError
from django.utils import timezone


def max_age(value):
    if value + 60 < timezone.now().year:
        raise ValidationError('Player cannot be more than 60 years old')

def min_age(value):
    if value + 7 > timezone.now().year:
        raise ValidationError('Player must be at least 7 years old')