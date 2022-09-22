from apps.Coin.models import Coins
from apps.Coin.serializer import CoinsSerializer
from rest_framework import viewsets


class CoinsView(viewsets.ModelViewSet):
    """List of all cryptocurrencies in different currencies"""
    serializer_class = CoinsSerializer
    queryset = Coins.objects.all()
