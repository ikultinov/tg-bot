import datetime
import telebot
import pytz
import time
import os
from dotenv import load_dotenv 
import requests



load_dotenv()

TOKEN = os.getenv('TOKEN')
URL = 'https://api.telegram.org/bot'

bot = telebot.TeleBot(TOKEN)


def send_message():
    now = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
    chat_id = '' # this group_id
    text = 'Privet meou!'
    bot.send_message(chat_id=chat_id, text=text)


def send_photo_file():
    chat_id = '@kotiki_for_Max' # this chanel
    bot.send_photo(chat_id=chat_id, photo=open('1.jpeg', 'rb'))


while True:
    now = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
    if now.hour == 10 and now.minute == 00 and now.second == 0:
        send_message()
        send_photo_file()
        time.sleep(1)
