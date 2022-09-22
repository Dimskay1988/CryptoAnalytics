from rest_framework import serializers
from .models import Profile, MessageProfile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class MessageProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageProfile
        fields = '__all__'
