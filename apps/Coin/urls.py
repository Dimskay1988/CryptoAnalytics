from apps.Coin.views import CoinsView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'coin', CoinsView, basename='coins')


urlpatterns = router.urls

