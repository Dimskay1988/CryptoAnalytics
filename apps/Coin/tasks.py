from celery import shared_task
from pycoingecko import CoinGeckoAPI
from rest_framework.response import Response
from rest_framework import status
from apps.Coin.models import Coins

cg = CoinGeckoAPI()


@shared_task
def update_coin():
    data = cg.get_price(ids=['bitcoin', 'litecoin', 'ethereum', 'solana', 'cardano', 'tether'],
                        vs_currencies=['usd', 'eur', 'uah', 'cny'])
    for name in data:
        Coins.objects.update_or_create(name=name, defaults={'usd': data[name]['usd'], 'eur': data[name]['eur'],
                                                            'uah': data[name]['uah'], 'cny': data[name]['cny']})
    return Response(status=status.HTTP_200_OK)
