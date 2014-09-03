__author__ = 'kjb9rk'


from flask import Flask
import os
from flask.ext.sqlalchemy import SQLAlchemy
from netflix_finder import get_netflix_movies
from amazon_finder import get_amazon_movies

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
db = SQLAlchemy(app)


def init_db():
    db.create_all()
    for item in get_netflix_movies():
        movie = Movie(item.title, item.rating, item.synopsis, "Netflix")
        movie.score = item.score
        db.session.add(movie)
        db.session.commit()
    for item in get_amazon_movies():
        movie = Movie(item.title, -1, "", "Amazon")
        db.session.add(movie)
        db.session.commit()


class Movie(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    rating = db.Column(db.String)
    synopsis = db.Column(db.String)
    site = db.Column(db.String)
    score = db.Column(db.String)

    def __init__(self, title, rating, synopsis, site):
        self.title = title
        self.rating = rating
        self.synopsis = synopsis
        self.site = site
        self.score = 0

    def __repr__(self):
        return "<Movie: \'%s\'>" % self.title

    def serialize(self):
        return {
            'title': self.title,
            'rating': self.rating,
            'synopsis': self.synopsis,
            'site': self.site,
            'keywords': self.get_keywords()
        }

    def get_keywords(self):
        return str(self.synopsis).split(" ")