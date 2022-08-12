import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()


class CoinsList(APIView):  # список всех криптовалют
    http_method_names = ["get"]
    """" Список вчех криптовалют"""
    def get(self, request):
        data = requests.get("https://api.coingecko.com/api/v3/coins/list?include_platform=true").json()
        return Response(data, status=status.HTTP_200_OK)


class CoinsPrice(APIView):  # получение одной крипто валюты по id

    def get(self, request, coin_id):
        data = requests.get(f"https://api.coingecko.com/api/v3/coins/{coin_id}").json()
        return Response(data, status=status.HTTP_200_OK)
        # return Response(data.get("market_data").get("current_price"), status=status.HTTP_200_OK)


class List_Currencies(APIView):
    """Список всех валют"""
    def get(self, request):
        data = cg.get_supported_vs_currencies()
        return Response(data, status=status.HTTP_200_OK)
