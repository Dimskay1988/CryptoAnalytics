from rest_framework import serializers
from .models import Coins



class CoinsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coins
        fields = '__all__'

