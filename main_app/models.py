from django.db import models
from django.urls import reverse

class Dev(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    age = models.IntegerField()
    bio = models.TextField(max_length=400)
    remote = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'dev_id': self.id})
