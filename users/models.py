
from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    telegram = models.CharField(max_length=150, verbose_name='Telegram')
    chat_id = models.CharField(max_length=255, default=None, verbose_name='Chat ID', **NULLABLE)
    REQUIRED_FIELDS = ["email", "telegram"]