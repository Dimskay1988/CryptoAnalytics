from rest_framework.viewsets import ModelViewSet
from apps.Employees.models import Profile, MessageProfile
from apps.Employees.serializers import ProfileSerializer, MessageProfileSerializer


class ProfileViewSet(ModelViewSet):
    """list of all telegram bot users"""
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class MessageProfileViewSet(ModelViewSet):
    """Список всех пользователей"""
    serializer_class = MessageProfileSerializer
    queryset = MessageProfile.objects.all()
