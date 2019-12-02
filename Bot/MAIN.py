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


def main(command_num):
    if command_num == 1:
        film = input()
        url = 'https://okko.tv/movie/' + film
        description = get_description(get_html(url))
        print(description)
    elif command_num == 2:
        url = 'https://okko.tv/collection/top250kinopoisk'
        random_movie = random.choice(get_movies(get_html(url)))
        print(random_movie)
    elif command_num == 3:
        actor = input()
        url = 'https://okko.tv/person/' + actor
        movies = random.choice(get_movies(get_html(url)))
        print(movies)


if __name__ == '__main__':
    num = int(input())
    main(num)


