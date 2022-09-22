from django.db import models
from django.utils import timezone

class Coins(models.Model):
    name = models.CharField(max_length=30)
    usd = models.FloatField(max_length=30)
    eur = models.FloatField(max_length=30)
    uah = models.FloatField(max_length=30)
    cny = models.FloatField(max_length=30)
    updated_at = models.DateTimeField(auto_now=timezone.now())

    def __str__(self):
        return self.name
