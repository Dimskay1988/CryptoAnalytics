from django.contrib import admin
from apps.Coin.models import Coins


# @admin.register(Currency)
# class CurrencyAdmin(admin.ModelAdmin):
#     pass
#
#
@admin.register(Coins)
class CoinsAdmin(admin.ModelAdmin):
    list_display = ('name', 'usd', 'eur', 'uah', 'cny', 'updated_at')
    fields = ['name', 'usd', 'eur', 'uah', 'cny', 'updated_at']
    search_fields = ['name']
