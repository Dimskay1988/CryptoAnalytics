from django.db import models
from django.apps import apps


class Profile(models.Model):
    id_user = models.PositiveIntegerField(verbose_name='ID пользователя в сети', unique=True)
    name = models.TextField(verbose_name='Имя пользователя')

    def __str__(self):
        return f'#{self.id_user}{self.name}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Message (models.Model):
    profile = models.ForeignKey('Employees.Profile', verbose_name='Профиль', on_delete=models.PROTECT)
    text = models.TextField(verbose_name='Текст')
    created_at = models.DateField(verbose_name='Время получения', auto_now_add=True)

    def __str__(self):
        return f'Сообщение {self.pk} от {self.profile}'
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
