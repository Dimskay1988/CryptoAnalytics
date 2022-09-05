from pycoingecko import CoinGeckoAPI
from rest_framework import status
from rest_framework.response import Response
from .celery import app
from celery import shared_task
from celery.schedules import crontab

cg = CoinGeckoAPI()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')


@app.task
def list_currencies(self, request):
    data = cg.get_supported_vs_currencies()
    print(data)
    return Response(data, status=status.HTTP_200_OK)


@app.task
def test(arg):
    print(arg)


@app.task
def add(x, y):
    return x + y


@shared_task
def rename_widget(widget_id, name):
    pass
    # w = Widget.objects.get(id=widget_id)
    # w.name = name
    # w.save()
