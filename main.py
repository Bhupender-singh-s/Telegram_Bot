import os
import telebot
from keepmealive import keep_alive

API_KEY = os.environ['API_KEY']
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['Greet'])
def greet(message):
  bot.send_message(message.chat.id,"Hello there how can i help you")

@bot.message_handler(commands=['hello'])
def hello(message):
  bot.send_message(message.chat.id,"hello")

keep_alive()
bot.polling()
