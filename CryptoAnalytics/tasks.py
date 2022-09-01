from pycoingecko import CoinGeckoAPI
from rest_framework import status
from rest_framework.response import Response
from .celery import app
from celery import shared_task


cg = CoinGeckoAPI()


@app.task
def list_currencies(self, request):
    data = cg.get_supported_vs_currencies()
    print(data)
    return Response(data, status=status.HTTP_200_OK)


@app.task
def add(x, y):
    return x + y

@shared_task
def rename_widget(widget_id, name):
    pass
    # w = Widget.objects.get(id=widget_id)
    # w.name = name
    # w.save()
