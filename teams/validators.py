from django.core.exceptions import ValidationError
from django.utils import timezone


def up_to_current_year(value):
    if value > timezone.now().year:
        raise ValidationError('Established year cannot be in the future')