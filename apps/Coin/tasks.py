# from celery import shared_task
from pycoingecko import CoinGeckoAPI
from rest_framework.response import Response
from rest_framework import status
from apps.Coin.models import CoinsAll, Cryptocurrency, Coin
import schedule
import time

cg = CoinGeckoAPI()


def update_coin():
    data = cg.get_price(ids=['bitcoin', 'litecoin', 'ethereum', 'solana', 'cardano', 'tether'],
                        vs_currencies=['usd', 'eur', 'uah', 'cny'])
    for name in data:
        CoinsAll.objects.update_or_create(name=name, defaults={'usd': data[name]['usd'], 'eur': data[name]['eur'],
                                                               'uah': data[name]['uah'], 'cny': data[name]['cny']})
        currency = Cryptocurrency.objects.update_or_create(name=name)
        Coin.objects.create(id_cryptocurrency=currency[0],
                            usd=data[name]['usd'], eur=data[name]['eur'],
                            uah=data[name]['uah'], cny=data[name]['cny'])
    print('update_coin')


schedule.every(1).minutes.do(update_coin)

while True:
    schedule.run_pending()
    time.sleep(1)
