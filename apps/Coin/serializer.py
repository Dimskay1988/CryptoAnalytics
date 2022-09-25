from rest_framework import serializers
from .models import CoinsAll, Cryptocurrency, Coin


class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = ('id', 'id_cryptocurrency', 'usd', 'eur', 'uah', 'cny', 'created_at')


class StatisticsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cryptocurrency
        fields = '__all__'


class CoinsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinsAll
        fields = '__all__'
