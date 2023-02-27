import os
import telebot
import requests
import json
import time
from keepmealive import keep_alive


NewsApi = os.environ['NewsApi']
API_KEY = os.environ['API_KEY']
bot = telebot.TeleBot(API_KEY)
search = input()

@bot.message_handler(commands=['Greet'])
def greet(message):
  bot.send_message(message.chat.id,"Thank you for choosing our services")

@bot.message_handler(commands=['topnews'])
def topnews_handler(message):
    response = requests.get(f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NewsApi}')
    news_data = response.json()
    articles = news_data['articles'][:3]
    for article in articles:
        bot.send_message(message.chat.id, f"{article['title']}\n{article['url']}")
        time.sleep(1)
    bot.send_message(message.chat.id,"Thank you for choosing our services")
  
@bot.message_handler(commands=['bbc'])
def business(message):
    response = requests.get(f'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={NewsApi}')
    news_data = response.json()
    articles = news_data['articles'][:3]
    for article in articles:
        bot.send_message(message.chat.id, f"{article['title']}\n{article['url']}")
        time.sleep(1)
    bot.send_message(message.chat.id,"Thank you for choosing our services")

@bot.message_handler(commands=['search'])
def search(message):
    response = requests.get(f'https://newsapi.org/v2/top-headlines?sources={search}&apiKey={NewsApi}')
    news_data = response.json()
    articles = news_data['articles'][:3]
    for article in articles:
        bot.send_message(message.chat.id, f"{article['title']}\n{article['url']}")
        time.sleep(1)
    bot.send_message(message.chat.id,"Thank you for choosing our services")
  
@bot.message_handler(commands=['start'])
def help_handler(message):
    bot.reply_to(message,"Here are the available commands:\n"
                 "\n"
                 "General things about bot:"
                          "~ /stop - Start the bot\n"
                          "~ /help - Show this help message\n"
                          "~ /about - Learn more about the bot\n"
                 "\n"
                 "Here are some commands for news on category:\n"
                          "~ /topnews - Get some information\n"
                          "~ /bbc - Get the latest news\n"
                
                )
keep_alive()
bot.polling()
