from apps.Coin.views import CoinsView, LastHourView, ListCoinView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'coin', CoinsView, basename='coins')
router.register(r'last_hour', LastHourView, basename='last_hour')
router.register(r'cryptocurrency', ListCoinView, basename='cryptocurrency')

urlpatterns = router.urls

