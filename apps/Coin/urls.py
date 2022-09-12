from django.urls import path
from apps.Coin.views import CoinsView, CoinsPrice, CoinTop

from rest_framework.routers import DefaultRouter

urlpatterns = [

    path('coins/', CoinsView.as_view({'get': 'list'})),
    path('top/', CoinTop.as_view()),
    path('coins/<str:coin_id>/price/', CoinsPrice.as_view()),
]


