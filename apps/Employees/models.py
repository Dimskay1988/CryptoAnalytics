from locale import currency

from django.db import models
from django.apps import apps


class Profile(models.Model):
    id_user = models.PositiveIntegerField(verbose_name='ID пользователя в сети', unique=True)
    name = models.TextField(verbose_name='Имя пользователя', null=True)
    surname = models.TextField(verbose_name='Фамилия пользователя', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'#{self.id_user}{self.name}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class MessageProfile(models.Model):
    currency = models.TextField(verbose_name='Отслеживаемая криптовалют')
    coin = models.TextField(verbose_name='В валюте')
    price = models.FloatField(max_length=30, verbose_name='Стоимость')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    id_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'#{self.id_profile}'

    class Meta:
        verbose_name = 'Сообщение от профиля'
        verbose_name_plural = 'Сообщения от профилей'
