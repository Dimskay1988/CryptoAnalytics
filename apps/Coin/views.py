import json
import requests
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from pycoingecko import CoinGeckoAPI
from apps.Coin.models import ListCurrencies, Coins
from apps.Coin.serializer import CoinsSerializer, ListcurrenciesSerializer
from rest_framework import viewsets

cg = CoinGeckoAPI()


class CoinsList(APIView):  # список всех криптовалют
    """" Список вcех криптовалют"""

    def get(self, request):
        data = requests.get("https://api.coingecko.com/api/v3/coins/list").json()
        return Response(data, status=status.HTTP_200_OK)

    # def create(self, validated_data):
    #     data = requests.get("https://api.coingecko.com/api/v3/coins/list?include_platform=true").json()
    #     return Coins.objects.create(**validated_data)


class CoinsPrice(APIView):  # получение одной крипто валюты по id

    def get(self, request, coin_id):
        data = requests.get(f"https://api.coingecko.com/api/v3/coins/{coin_id}").json()
        return Response(data, status=status.HTTP_200_OK)
        # return Response(data.get("market_data").get("current_price"), status=status.HTTP_200_OK)


class List_Currencies(APIView):
    """Список всех валют"""

    def get(self, request):
        data = cg.get_supported_vs_currencies()
        for i in data:
            ListCurrencies.objects.create(currency=i)
        return Response(data, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    """
    Валюта
    """
    serializer_class = CoinsSerializer
    queryset = ListCurrencies.objects.all()
    def get_object(self):
        data = ListCurrencies.objects.all()
        return Response(data)


