from pycoingecko import CoinGeckoAPI
from apps.Coin.models import CoinsAll, Cryptocurrency, Coin
# from apps.Coin.management.commands import bot
# import threading
cg = CoinGeckoAPI()


# async def start():
#     bot.start()
#
#
# def run_bot(start):
#     job_thread = threading.Thread(target=start)
#     job_thread.start()


def update_coin():
    data = cg.get_price(ids=['bitcoin', 'litecoin', 'ethereum', 'solana', 'cardano', 'tether'],
                        vs_currencies=['usd', 'eur', 'uah', 'cny'])
    for name in data:
        CoinsAll.objects.update_or_create(name=name, defaults={'usd': data[name]['usd'], 'eur': data[name]['eur'],
                                                               'uah': data[name]['uah'], 'cny': data[name]['cny']})
        Cryptocurrency.objects.update_or_create(name=name)
        Coin.objects.create(id_cryptocurrency=Cryptocurrency.objects.filter(name=name)[0],
                            usd=data[name]['usd'], eur=data[name]['eur'],
                            uah=data[name]['uah'], cny=data[name]['cny'])

    print('Обновился курс')

