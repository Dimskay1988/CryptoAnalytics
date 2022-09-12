from rest_framework import serializers
from .models import Coins
import io
from rest_framework.parsers import JSONParser


class CoinsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coins
        fields = '__all__'

#
# class CurrencySerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Currency
#         fields = ['id_coin', 'usd', 'eur', 'uah', 'cny']
