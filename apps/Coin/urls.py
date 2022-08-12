from django.urls import path
from .views import CoinsList, CoinsPrice,List_Currencies



urlpatterns = [
    path('coins/', CoinsList.as_view()),
    path('praize/', List_Currencies.as_view()),
    path('coins/<str:coin_id>/price/', CoinsPrice.as_view()),
]

