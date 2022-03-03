from datetime import datetime
import django
from django.conf import settings
from django.db import models


class Post(models.Model):

    def __str__(self):
        return f'{self.votes} {self.author} {self.creator}'

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        default=None
    )

    created = models.DateTimeField(
        default=django.utils.timezone.now
    )
    
    author = models.CharField(max_length=200 )
    text = models.CharField(max_length=1000)
    votes = models.BigIntegerField(default=0)

class Vote(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        default=None
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.DO_NOTHING
    )

    vote = models.SmallIntegerField(default=0)

    class Meta:
        unique_together = ('user', 'post',)

    def __str__(self):
        return f'{self.user}: {self.vote}'
