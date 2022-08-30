import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CryptoAnalytics.settings')
app = Celery('CryptoAnalytics')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'add-every-minute': {
        'task': 'tasks.add',
        'schedule': crontab(minute='*/1'),
        'args': (12, 12),
    },
}

