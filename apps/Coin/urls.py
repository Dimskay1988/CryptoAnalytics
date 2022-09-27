from apps.Coin.views import CoinsView, LastHourView, ListCoinView, LastDayView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'coin', CoinsView, basename='coins')
router.register(r'last_hour', LastHourView, basename='last_hour')
router.register(r'last_day', LastDayView, basename='last_day')
router.register(r'cryptocurrency', ListCoinView, basename='cryptocurrency')

urlpatterns = router.urls

