from django.urls import path
from .views import CoinsList, CoinsPrice, List_Currencies, UserViewSet
from apps.Coin.views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')



urlpatterns = [

    path('coins/', CoinsList.as_view()),
    path('praize/', List_Currencies.as_view()),
    path('coins/<str:coin_id>/price/', CoinsPrice.as_view()),
]

urlpatterns += router.urls
