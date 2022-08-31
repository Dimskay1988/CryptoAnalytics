from django.urls import path, include
from apps.Employees.views import UsersViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'users', UsersViewSet, basename='Users')

urlpatterns = router.urls
