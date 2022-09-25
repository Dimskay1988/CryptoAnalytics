from apps.Coin.models import Coins
from apps.Coin.serializer import CoinsSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class CoinsView(viewsets.ModelViewSet):
    """List of all cryptocurrencies in different currencies"""
    serializer_class = CoinsSerializer
    queryset = Coins.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
