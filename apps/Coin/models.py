from django.db import models


class ListCurrencies(models.Model):
    currency = models.CharField(max_length=20)

    def __str__(self):
        return self.currency


class Coins(models.Model):
    id = models.TextField(primary_key=True, max_length=130)
    symbol = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    platforms = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.name
