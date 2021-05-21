from django.contrib.auth.models import User
from django.db import models

class Communaute(models.Model):
    name = models.CharField(max_length=200)
    abonnes = models.ManyToManyField(User)

    def __str__(self):
        return self.name