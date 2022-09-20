from pycoingecko import CoinGeckoAPI
from rest_framework import status
from rest_framework.response import Response
from .celery import app
from celery import shared_task

cg = CoinGeckoAPI()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')


@app.task
def supper_sum(x, y):
    return x + y


# @app.task
# def list_currencies(self, request):
#     data = cg.get_supported_vs_currencies()
#     print(data)
#     return Response(data, status=status.HTTP_200_OK)


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


#######################################

from CryptoAnalytics.celery import app


@app.task
def supper_sum(x, y):
    return x + y


from celery.schedules import crontab

app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': 30.0,
        'args': (16, 16)
    },
}


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test.s('Happy Mondays!'),
    )


@app.task
def test(arg):
    print(arg)


@app.task
def add(x, y):
    z = x + y
    print(z)
