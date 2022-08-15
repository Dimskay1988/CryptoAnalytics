from django.contrib import admin
from apps.Coin.models import ListCurrencies, Coins


@admin.register(ListCurrencies)
class ListCurrenciesAdmin(admin.ModelAdmin):
    pass


@admin.register(Coins)
class CoinsAdmin(admin.ModelAdmin):
    pass
