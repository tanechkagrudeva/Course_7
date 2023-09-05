from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("habits", "0002_rename_is_related_habit_related"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="duration",
            field=models.IntegerField(verbose_name="Длительность в секундах"),
        ),
        migrations.AlterField(
            model_name="habit",
            name="period",
            field=models.IntegerField(verbose_name="Период"),
        ),
    ]