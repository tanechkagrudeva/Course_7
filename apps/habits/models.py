from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    """
    Model representing a habit.

    Fields:
    - owner (ForeignKey): The user associated with the habit.
    - place (CharField): The place where the habit is performed.
    - time (TimeField): The time when the habit is performed.
    - action (CharField): The action of the habit.
    - is_pleasant (BooleanField): Indicates whether the habit is pleasant or not.
    - related_habit (ForeignKey): A related habit, if any. Can be NULL.
    - frequency (PositiveIntegerField): The frequency of the habit.
    - reward (CharField): The reward for completing the habit. Can be NULL.
    - eta (PositiveIntegerField): The estimated time required to complete the habit.
    - is_public (BooleanField): Indicates whether the habit is public or not.
    """
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)
    place = models.CharField(max_length=50, verbose_name='место', help_text='отвечает на вопрос где')
    time = models.TimeField(verbose_name='время')
    action = models.CharField(max_length=100, verbose_name='действие')
    is_pleasant = models.BooleanField(verbose_name='приятность привычки', default=False)
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL,
                                      verbose_name='связанная привычка', **NULLABLE)
    frequency = models.PositiveIntegerField(default=1, verbose_name='периодичность', help_text="не больше 7")
    reward = models.CharField(max_length=250, verbose_name='вознаграждение', **NULLABLE)
    eta = models.PositiveIntegerField(verbose_name='время на выполнение', help_text="не больше 120 секунд")
    is_public = models.BooleanField(verbose_name='публичность привычки', default=False)

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
        ordering = ('action',)