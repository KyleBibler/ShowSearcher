from flask import Flask, render_template, jsonify
from models import Movie

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/movies/movie-list.json')
def movie_list():
    movies = []
    for i in Movie.query.all():
        movies += [i.serialize()]
    return jsonify(movies=movies)


if __name__ == '__main__':
    app.run()
