from rest_framework import serializers
from .models import ListCurrencies, Coins


class ListcurrenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListCurrencies
        fields = ('id', 'currency')


class CoinsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coins
        fields = ('id', 'symbol', 'name')
