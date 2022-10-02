from pycoingecko import CoinGeckoAPI
# from rest_framework.response import Response
# from rest_framework import status
# from apps.Coin.models import CoinsAll, Cryptocurrency, Coin


cg = CoinGeckoAPI()

# from apps.Coin.management.commands import bot

# def start_bot():
#     # bot.start()
#     return print('Старт Bot')


def update_coin():
    data = cg.get_price(ids=['bitcoin', 'litecoin', 'ethereum', 'solana', 'cardano', 'tether'],
                        vs_currencies=['usd', 'eur', 'uah', 'cny'])
    print(data)
    # for name in data:
    #     CoinsAll.objects.update_or_create(name=name, defaults={'usd': data[name]['usd'], 'eur': data[name]['eur'],
    #                                                            'uah': data[name]['uah'], 'cny': data[name]['cny']})
#         Cryptocurrency.objects.update_or_create(name=name)
#         Coin.objects.create(id_cryptocurrency=Cryptocurrency.objects.filter(name=name)[0],
#                             usd=data[name]['usd'], eur=data[name]['eur'],
#                             uah=data[name]['uah'], cny=data[name]['cny'])
#
#     return Response(status=status.HTTP_200_OK)

#
# schedule.every(1).minutes.do(update_coin)
# schedule.every(3).seconds.do(start_bot)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)


def job():
    print("I'm working...")




