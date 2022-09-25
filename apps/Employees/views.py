from rest_framework.viewsets import ModelViewSet
from apps.Employees.models import Profile, MessageProfile
from apps.Employees.serializers import ProfileSerializer, MessageProfileSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class ProfileViewSet(ModelViewSet):
    """list of all telegram bot users"""
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

class MessageProfileViewSet(ModelViewSet):
    """Список всех пользователей"""
    serializer_class = MessageProfileSerializer
    queryset = MessageProfile.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]