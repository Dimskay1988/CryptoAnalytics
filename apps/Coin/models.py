from django.db import models


class Coins(models.Model):
    name = models.CharField(max_length=30)
    usd = models.FloatField(max_length=30)
    eur = models.FloatField(max_length=30)
    uah = models.FloatField(max_length=30)
    cny = models.FloatField(max_length=30)

    def __str__(self):
        return self.name
