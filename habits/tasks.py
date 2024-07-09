from celery import shared_task
from django.conf import settings
from .models import Habit
import requests


@shared_task
def send_telegram_message(chat_id, text):
    url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    requests.post(url, data=payload)


@shared_task
def send_habit_reminders():
    habits = Habit.objects.all()
    for habit in habits:
        message = f"Don't forget to {habit.action} at {habit.time} in {habit.place}!"
        send_telegram_message.delay(habit.user.telegram_chat_id, message)
