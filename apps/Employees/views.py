
from rest_framework.viewsets import ModelViewSet
from apps.Employees.models import CustomUser
from apps.Employees.serializers import UserSerializer


class UsersViewSet(ModelViewSet):
    """Список всех пользователей"""
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()


