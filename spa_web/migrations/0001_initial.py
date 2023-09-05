from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Place",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("place", models.CharField(max_length=100, verbose_name="Место")),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Habit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("time", models.TimeField(auto_now_add=True, verbose_name="Время")),
                ("action", models.CharField(max_length=100, verbose_name="Действие")),
                (
                    "is_pleasant",
                    models.BooleanField(default=False, verbose_name="Приятная привычка"),
                ),
                ("period", models.IntegerField(default=0, verbose_name="Период")),
                (
                    "reward",
                    models.CharField(max_length=100, verbose_name="Вознаграждение"),
                ),
                (
                    "duration",
                    models.IntegerField(
                        default=0, verbose_name="Длительность в секундах"
                    ),
                ),
                (
                    "is_public",
                    models.BooleanField(default=False, verbose_name="Публичный"),
                ),
                (
                    "is_related",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="habits.habit",
                        verbose_name="Связанная привычка",
                    ),
                ),
                (
                    "place",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="habits.place",
                        verbose_name="Место",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
        ),
    ]