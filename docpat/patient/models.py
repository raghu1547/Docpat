
# Create your models here.
from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

    def save(self):
        super().save()

    def __str__(self):
        return self.user.username
