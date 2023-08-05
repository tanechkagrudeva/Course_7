from django.db import models

from apps.users.models import User

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    place = models.CharField(max_length=255, verbose_name='Place')
    time = models.DateTimeField(verbose_name='Time')
    action = models.CharField(max_length=255, verbose_name='Action')
    is_pleasant = models.BooleanField(default=False, verbose_name='Is pleasant')
    related_habit = models.ForeignKey('Habit', on_delete=models.SET_NULL, **NULLABLE, verbose_name='Related habit')
    # Frequency in days
    frequency = models.IntegerField(default=1, verbose_name='Frequency')
    reward = models.CharField(max_length=255, **NULLABLE, verbose_name='Reward')
    # Execution_time in seconds
    execution_time = models.IntegerField(**NULLABLE, verbose_name='Execution time')
    is_public = models.BooleanField(default=False, verbose_name='Is public')

    def __str__(self):
        return f'I will {self.action} at {self.time} in {self.place}'

    class Meta:
        verbose_name = 'habit'
        verbose_name_plural = 'habits'
