from django.db import models


class Animal(models.Model):

    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

    PRIORITY = ((LOW, 'low'), (MEDIUM, 'medium'), (HIGH, 'high'))

    name = models.CharField(max_length=20)
    image_url = models.URLField()
    description = models.TextField(max_length=250)
    is_cured = models.BooleanField(default=False)
    priority = models.CharField(max_length=6, choices=PRIORITY)


    def __str__(self):
        return f'{self.id}; {self.name}; {self.is_cured}'
