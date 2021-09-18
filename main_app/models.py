from django.db import models
from django.db.models import aggregates

class Dev(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    age = models.IntegerField()
    bio = models.TextField(max_length=400)
    remote = models.BooleanField()
