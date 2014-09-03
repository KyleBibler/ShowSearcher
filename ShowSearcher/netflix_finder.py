__author__ = 'kjb9rk'

from bs4 import BeautifulSoup
from urllib2 import urlopen

MAX_PAGES = 1


def get_netflix_movies():
    page_count = 1
    movie_db = []
    try:
        while page_count <= MAX_PAGES:
            url = "http://instantwatcher.com/titles/all?page=" + \
                  str(page_count) + "&view=synopsis&popups=1&infinite=0"
            soup = BeautifulSoup(urlopen(url))
            title_list = soup.find_all('li', class_='title-list-item')
            for movie_info in title_list:
                item_list = []
                for item in movie_info.find_all():
                    if item.string:
                        item_list += [item.string.encode('utf-8').strip()]
                item_list = item_list[:-3] + item_list[-1:]
                movie = NetflixMovie(item_list)
                movie_db += [movie]
            page_count += 1
    except Exception:
        movie_db = []
    return movie_db


class NetflixMovie:

    def __init__(self, info_list):
        self.title = info_list[0]
        self.year = info_list[1]
        self.rating = info_list[2]
        self.score = info_list[3]
        self.synopsis = info_list[len(info_list)-1]

    def __repr__(self):
        report = "<Movie: %s>" % self.title
        return report

    def title(self):
        return self.title

    def synopsis(self):
        return self.synopsis

    def get_keywords(self):
        return str(self.synopsis).split(" ")


if __name__ == '__main__':
    for mov in get_netflix_movies():
        print mov