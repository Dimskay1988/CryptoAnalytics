from rest_framework import serializers
from .models import Profile, MessageProfile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'username', 'password', 'id_telegram', 'created_at']


class MessageProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageProfile
        fields = '__all__'
