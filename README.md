<img src="https://resources.workable.com/wp-content/uploads/2019/03/hiring-managers-recruiters.jpg">

## Hire Manager's Dev-collector
https://devcollector.herokuapp.com/

## User Stories
- Fully functional database that allows for users to Create, Read, Update and Delete.
- App include one-to-one and many-to-many associations.
- App include authentication processes.
- AWS Photo Uploads.

## Models
```
ROUNDS = (
    ('1st', 'First Round'),
    ('2nd', 'Second Round'),
    ('3rd', 'Final Round')
)

class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('languages_detail', kwargs={'pk': self.id})

class Dev(models.Model):
    name = models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    age = models.IntegerField()
    bio = models.TextField(max_length=400)
    remote = models.BooleanField(default=False)
    languages = models.ManyToManyField(Language)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'dev_id': self.id})

class Interview(models.Model):
    date = models.DateField('Interview Date')
    stage = models.CharField(max_length=3, choices=ROUNDS, default=ROUNDS[0][0])
    dev = models.ForeignKey(Dev, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.get_stage_display()} on {self.date}'

class Photo(models.Model):
    url = models.CharField(max_length=200)
    dev = models.ForeignKey(Dev, on_delete=models.CASCADE)

    def __str__(self):
        return f'Photo of dev_id: {self.dev_id} @{self.url}'
```

![Alt text](Users/Hamilton/Desktop/django-project)
