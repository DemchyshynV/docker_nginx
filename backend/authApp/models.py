from django.db import models


# Create your models here.

class InviteModel(models.Model):
    class Meta:
        db_table = 'invite'

    uuid = models.CharField(max_length=255, unique=True)
    isMentor = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
