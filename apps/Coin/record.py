from pycoingecko import CoinGeckoAPI
import time
import threading
from models import ListCurrencies


cg = CoinGeckoAPI()


def update(**kwargs):
    data = cg.get_supported_vs_currencies()
    for i in data:
        ListCurrencies.objects.update(currency=i)
    print('OK')


# while True:
#     time.sleep(5)
#     thread = threading.Thread(target=update)
#     thread.start()
