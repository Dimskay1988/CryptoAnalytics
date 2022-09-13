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

