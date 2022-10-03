from rest_framework import serializers
from .models import CoinsAll, Cryptocurrency, Coin


class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptocurrency
        fields = '__all__'


class CoinSerializer(serializers.ModelSerializer):
    id_cryptocurrency = StatisticsSerializer(many=False)

    class Meta:
        model = Coin
        fields = ('id', 'id_cryptocurrency', 'usd', 'eur', 'uah', 'cny', 'created_at')


class CoinsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinsAll
        fields = '__all__'
