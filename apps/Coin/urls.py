from django.urls import path
from apps.Coin.views import CoinsList, CoinsPrice, CoinTop, CoinsTest
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'test', CoinsTest, basename='comment')

urlpatterns = [
    path('coins/', CoinsList.as_view()),
    # path('praize/', List_Currencies.as_view()),
    # path('coins/<str:coin_id>/price/', CoinsPrice.as_view()),
    path('top/', CoinTop.as_view()),
]

urlpatterns += router.urls
