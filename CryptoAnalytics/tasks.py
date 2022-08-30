from CryptoAnalytics.celery import app
from pycoingecko import CoinGeckoAPI
from apps.Coin.models import ListCurrencies
import requests
from rest_framework import status
from rest_framework.response import Response

cg = CoinGeckoAPI()


@app.task
def list_currencies(self, request):
    data = cg.get_supported_vs_currencies()
    print(data)
    return Response(data, status=status.HTTP_200_OK)

@app.task
def supper_sum(x, y):
    return x + y
