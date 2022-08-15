from django.db import models


class ListCurrencies(models.Model):
    currency = models.CharField(max_length=20)

    def __str__(self):
        return self.currency


class Coins(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    symbol = models.CharField(max_length=30)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
