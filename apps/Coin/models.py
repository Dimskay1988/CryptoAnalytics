from django.db import models


class Coins(models.Model):
    name = models.CharField(max_length=30)
    usd = models.FloatField(max_length=30)
    eur = models.FloatField(max_length=30)
    uah = models.FloatField(max_length=30)
    cny = models.FloatField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
