# -*- coding: utf-8 -*-
from config import token
import telebot

URL = 'https://api.telegram.org/bot'+token+'/'

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)
