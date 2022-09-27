from apps.Coin.models import CoinsAll, Cryptocurrency, Coin
from apps.Coin.serializer import CoinsSerializer, StatisticsSerializer, CoinSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class CoinsView(viewsets.ModelViewSet):
    """
    The current rate of cryptocurrencies
    """
    serializer_class = CoinsSerializer
    queryset = CoinsAll.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class LastHourView(viewsets.ModelViewSet):
    """
    Statistics for the last hour
    """
    serializer_class = CoinSerializer
    queryset = Coin.objects.all().order_by("-created_at")[:360]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class LastDayView(viewsets.ModelViewSet):
    """
    Statistics for the last day
    """
    serializer_class = CoinSerializer
    queryset = Coin.objects.all().order_by("-created_at")[:8640]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListCoinView(viewsets.ModelViewSet):
    """
    Full unloading of cryptocurrency
    """
    serializer_class = CoinSerializer
    queryset = Coin.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

