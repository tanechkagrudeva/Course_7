import datetime
from os import getenv
from datetime import datetime, timedelta
import requests
from celery import shared_task

from apps.habits.models import Habit


@shared_task
def send_tg_notification():

    # checking the time
    current_time = datetime.now().time()
    start_notification_time = datetime.now() - timedelta(minutes=1)
    # geting the habit list where time is greater than start time or equal
    habits_list = Habit.objects.filter(time__gte=start_notification_time)
    for habit in habits_list:
        if habit.time <= current_time:
            params = {
                # 'chat_id': User.objects.get(email=habit.owner).chat_id,
                'chat_id': getenv('CHAT_ID'),
                'text': f"Я буду {habit.action} {habit.place} в {habit.time} "
                        f"и получу за это возможность {habit.reward if habit.reward else habit.related_habit}\n"
            }
            try:
                print('отправка')
                requests.get(
                    f'https://api.telegram.org/bot{getenv("TG_API_KEY")}/sendMessage',
                    params=params
                )
            except Exception as err:
                print(err)