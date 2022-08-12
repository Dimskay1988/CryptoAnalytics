from django.db import models


class ListCurrencies(models.Model):
    currency = models.CharField(max_length=20)

    def __str__(self):
        return self.currency

# Create your models here.
