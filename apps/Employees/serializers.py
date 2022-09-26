from rest_framework import serializers
from .models import Profile, MessageProfile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'password', 'username', 'id_telegram', 'email')
        # fields = ['id', 'username', 'password', 'id_telegram', 'created_at']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'id_telegram', 'password', 'username', 'email')

    def create(self, validated_data):
        id_telegram = validated_data['id_telegram']
        username = validated_data['username']
        password = validated_data['password']
        repeat_password = validated_data['repeat_password']
        if password != repeat_password:
            raise serializers.ValidationError(
                {'password': 'Пароли не совпадают'})
        user = Profile(username=username, id_telegram=id_telegram)
        user.set_password(password)
        user.save()
        return user


class MessageProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageProfile
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True,
                                     style={'input_type': 'password'})
    repeat_password = serializers.CharField(write_only=True,
                                            style={'input_type': 'password'})

    class Meta:
        model = Profile
        fields = [
            'username',
            'password',
            'repeat_password',
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        repeat_password = validated_data['repeat_password']
        if password != repeat_password:
            raise serializers.ValidationError(
                {'password': 'Пароли не совпадают'})
        user = Profile(username=username)
        user.set_password(password)
        user.save()
        return user
