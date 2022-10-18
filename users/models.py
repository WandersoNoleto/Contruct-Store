from tabnanny import verbose

from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    choices_position = {
        ('V', 'Vendedor'),
        ('G', 'Gerente')
    }
    position = models.CharField(
        verbose_name = "Cargo",
        max_length = 1,
        choices = choices_position
    )
