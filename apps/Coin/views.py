import json
import requests
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from pycoingecko import CoinGeckoAPI
from rest_framework.viewsets import ModelViewSet

from apps.Coin.models import Coins
from apps.Coin.serializer import CoinsSerializer
from rest_framework import viewsets

cg = CoinGeckoAPI()


class CoinsList(APIView):  # список всех криптовалют
    """" Список вcех криптовалют"""

    def get(self, request):
        data = requests.get("https://api.coingecko.com/api/v3/coins/list").json()
        for i in data:
            Coins.objects.create(name=i["name"])
        return Response(data, status=status.HTTP_200_OK)


class CoinsPrice(APIView):  # получение одной крипто валюты по id

    def get(self, request, coin_id):
        data = requests.get(f"https://api.coingecko.com/api/v3/coins/{coin_id}").json()
        return Response(data, status=status.HTTP_200_OK)
        # return Response(data.get("market_data").get("current_price"), status=status.HTTP_200_OK)


# class List_Currencies(APIView):
#     """Список всех валют"""
#
#     def get(self, request):
#         data = cg.get_supported_vs_currencies()
#         for i in data:
#             ListCurrencies.objects.create(currency=i)
#         return Response(data, status=status.HTTP_200_OK)

class CoinTop(APIView):
    def get(self, request):
        data = cg.get_price(ids=['bitcoin', 'litecoin', 'ethereum', 'solana', 'cardano', 'tether'],
                            vs_currencies=['usd', 'eur', 'uah', 'cny'])
        print(data.keys())
        for name in data:
            Coins.objects.update_or_create(name=name, defaults={'usd': data[name]['usd'], 'eur': data[name]['eur'],
                                           'uah': data[name]['uah'], 'cny': data[name]['cny']})
        return Response(data, status=status.HTTP_200_OK)


class CoinsView(viewsets.ModelViewSet):
    """Отслеживаемые криптовалюты"""
    serializer_class = CoinsSerializer
    queryset = Coins.objects.all()

    # def list(self, request):
    #     queryset = Coins.objects.all()
    #     serializer = CoinsSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def get(self, request):
    #     data = [coin.name for coin in Coins.objects.all()]
    #     return Response(data)
