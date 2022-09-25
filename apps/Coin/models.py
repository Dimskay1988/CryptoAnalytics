from django.db import models
from django.utils import timezone


class CoinsAll(models.Model):
    name = models.CharField(max_length=30)
    usd = models.FloatField(max_length=30)
    eur = models.FloatField(max_length=30)
    uah = models.FloatField(max_length=30)
    cny = models.FloatField(max_length=30)
    updated_at = models.DateTimeField(auto_now=timezone.now())

    def __str__(self):
        return self.name


class Cryptocurrency(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Coin(models.Model):
    id_cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
    usd = models.FloatField(max_length=30)
    eur = models.FloatField(max_length=30)
    uah = models.FloatField(max_length=30)
    cny = models.FloatField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id_cryptocurrency}'
