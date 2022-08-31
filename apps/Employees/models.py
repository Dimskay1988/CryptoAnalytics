from django.db import models
from django.contrib.auth.models import AbstractUser
from django.apps import apps
import uuid


def create_invite_code():
    return str(uuid.uuid4())[0:8]


class CustomUser(AbstractUser):
    token = models.CharField(max_length=8, unique=True, default=create_invite_code)

    def __str__(self):
        return self.username
