from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    id_user = models.PositiveIntegerField(verbose_name='ID user telegram', unique=True, null=True)
    name = models.TextField(verbose_name='Username', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    password = models.TextField(verbose_name='Password')

    def __str__(self):
        return f'#{self.id_user}{self.username}'

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


class MessageProfile(models.Model):
    currency = models.TextField(verbose_name='Tracked Cryptocurrency')
    coin = models.TextField(verbose_name='Coin')
    price = models.FloatField(max_length=30, verbose_name='Price')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date')
    id_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    tracking_status = models.TextField(verbose_name='Tracking status', null=True)

    def __str__(self):
        return f'#{self.id_profile}'

    class Meta:
        verbose_name = 'Profile message'
        verbose_name_plural = 'Messages from profiles'
