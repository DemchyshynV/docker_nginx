from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    class Meta:
        db_table = 'auth_user'
    email = models.EmailField(max_length=100, unique=True)
