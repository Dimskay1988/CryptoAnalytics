from rest_framework import serializers
from .models import ListCurrencies, Coins
import io
from rest_framework.parsers import JSONParser

class ListcurrenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListCurrencies
        fields = ('id', 'currency')


class CoinsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListCurrencies
        fields = "__all__"
