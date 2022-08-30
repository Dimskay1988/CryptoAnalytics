import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CryptoAnalytics.settings')
app = Celery('CryptoAnalytics')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

from celery.schedules import crontab

app.conf.beat_schedule = {
    'add-every-minute': {
        'task': 'tasks.add',
        'schedule': crontab(minute='*/1'),
        'args': (16, 16),
    },
}

