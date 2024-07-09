import telebot
import django
import os

from django.conf import settings
from django.contrib.auth import get_user_model
from dotenv import load_dotenv



load_dotenv()

# Настройка Django окружения
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

CustomUser = get_user_model()

# Инициализация бота
bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Пожалуйста, отправь мне свой username.")

@bot.message_handler(func=lambda message: True)
def get_chat_id(message):
    chat_id = message.chat.id
    username = message.text
    try:
        user = CustomUser.objects.get(username=username)
        user.telegram_chat_id = chat_id
        user.save()
        bot.reply_to(message, "Ваш Telegram Chat ID сохранен.")
    except CustomUser.DoesNotExist:
        bot.reply_to(message, "Пользователь с таким username не найден.")

bot.polling()
