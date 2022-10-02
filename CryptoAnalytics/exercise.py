import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CryptoAnalytics.settings')
django.setup()

import schedule
import time
from CryptoAnalytics.tasks import update_coin


schedule.every(1).minutes.do(update_coin)

while True:
    schedule.run_pending()
    time.sleep(1)
