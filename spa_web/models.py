from django.db import models
from users.models import User

NULLABLE = {"blank": True, "null": True}

class Place(models.Model):
    place = models.CharField(max_length=100, verbose_name="Место")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", **NULLABLE)

    def __str__(self):
        return f'{self.place}'

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name="Место")
    time = models.TimeField(auto_now_add=True, verbose_name="Время")
    action = models.CharField(max_length=100, verbose_name="Действие")
    is_pleasant = models.BooleanField(default=False, verbose_name="Приятная привычка")
    related = models.ForeignKey("Habit", on_delete=models.SET_NULL, verbose_name="Связанная привычка", **NULLABLE)
    period = models.IntegerField(verbose_name="Период")
    reward = models.CharField(max_length=100, verbose_name="Вознаграждение")
    duration = models.IntegerField(verbose_name="Длительность в секундах")
    is_public = models.BooleanField(default=False, verbose_name="Публичный")

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'


