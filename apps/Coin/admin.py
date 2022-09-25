from django.contrib import admin
from apps.Coin.models import CoinsAll, Cryptocurrency, Coin


@admin.register(Cryptocurrency)
class CryptocurrencyAdmin(admin.ModelAdmin):
    pass
    # list_display = ('name', 'usd', 'eur', 'uah', 'cny')
    # fields = ['name', 'usd', 'eur', 'uah', 'cny']
    # search_fields = ['name']

#
# @admin.register(Coin)
# class CoinAdmin(admin.ModelAdmin):
#     pass


@admin.register(CoinsAll)
class CoinsAdmin(admin.ModelAdmin):
    list_display = ('name', 'usd', 'eur', 'uah', 'cny', 'updated_at')
    fields = ['name', 'usd', 'eur', 'uah', 'cny', 'updated_at']
    search_fields = ['name']
