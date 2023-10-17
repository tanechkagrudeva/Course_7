from datetime import datetime, timedelta

import django
from django_celery_beat.models import PeriodicTask, IntervalSchedule


def get_schedule(action, frequency: int):
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=frequency,
        period=IntervalSchedule.DAYS,
    )
    try:
        PeriodicTask.objects.create(
            interval=schedule,
            name=f'{action} раз в {frequency} {"дня" if frequency < 5 else "день" if frequency == 1 else "дней"}',
            task='habit.tasks.send_tg_notification',  # name of task.
            expires=datetime.utcnow() + timedelta(seconds=30)
        )
    except django.core.exceptions.ValidationError as err:
        print(err)