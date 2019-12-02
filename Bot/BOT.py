import telebot
import lxml
import random
import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text  # Возвращает HTML-код станицы (url)


def get_description(html):
    soup = BeautifulSoup(html, 'lxml')
    p = soup.find('p', class_='_2EIQv')
    return p.text


def get_movies(html):
    soup = BeautifulSoup(html, 'lxml')
    headers = soup.find_all('header', class_='_1597i')

    movies = []

    for header in headers:
        movies.append(header.text)

    return movies


TOKEN = '659578316:AAH4pVc_QH9ZIY3n-gYm87Zd5AVtCuKxmIY'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hey, how are you doing?")


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Вот список команд:\n/start - приветствие.\n/help - помощь.\n/random - случайный фильм из Топ-250 КиноПоиска.\n/description - описание фильма. Название фильма нужно писать на английском языке, заменяя пробелы дефисами. Название должно следовать после команды.\n/actor – случайный фильм с определённым актёром. Имя актёра нужно писать на английском языке, заменяя пробелы дефисами. Имя должно следовать после команды.")


@bot.message_handler(commands=['random'])
def send_welcome(message):
    url = 'https://okko.tv/collection/top250kinopoisk'
    random_movie = random.choice(get_movies(get_html(url)))
    bot.reply_to(message, random_movie)


@bot.message_handler(commands=['description'])
def send_welcome(message):
    @bot.message_handler(content_types=['text'])
    def echo_all(message_movie):
        url = f'https://okko.tv/movie/{message_movie.text}'
        description = get_description(get_html(url))
        bot.reply_to(message, description)


@bot.message_handler(commands=['actor'])
def send_welcome(message):
    @bot.message_handler(content_types=['text'])
    def echo_all(message_actor):
        url = f'https://okko.tv/person/{message_actor.text}'
        random_movie = random.choice(get_movies(get_html(url)))
        bot.reply_to(message, random_movie)


bot.polling(none_stop=True, interval=0)



