import django
from django.conf import settings
from django.db import models

# Create your models here.
class Contact(models.Model):

    def __str__(self):
        return f'{self.name} {self.text[:50]}'

    name = models.CharField(max_length=200 )

    email = models.EmailField(max_length=254,null=False)

    text = models.CharField(max_length=1000)