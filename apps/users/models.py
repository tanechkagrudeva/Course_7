from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class User(AbstractUser):
    """

    Model representing a user.

    Fields:
    - email (EmailField): Email address of the user. Used for authentication.
    - chat_id (CharField): Telegram chat id for sending messages. Can be NULL.
    - avatar (ImageField): Avatar image of the user.
    """
    username = None
    email = models.EmailField(max_length=50, verbose_name='почта', unique=True)
    chat_id = models.IntegerField(verbose_name='chat id', unique=True, **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []