from rest_framework import serializers
from .models import Profile, MessageProfile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'id_user', 'name', 'surname']


class MessageProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageProfile
        fields = ['id', 'id_profile', 'coin', 'currency', 'created_at']
