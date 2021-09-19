from django.db import models
from django.urls import reverse

ROUNDS = (
    ('1st', 'First Round'),
    ('2nd', 'Second Round'),
    ('3rd', 'Final Round')
)

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

class Interview(models.Model):
    date = models.DateField('Interview Date:')
    stage = models.CharField(max_length=3, choices=ROUNDS, default=ROUNDS[0][0])
    dev = models.ForeignKey(Dev, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_stage_display()} on {self.date}'
