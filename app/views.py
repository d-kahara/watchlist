from flask import render_template
from app import app

from .request import get_movies


# Views
@app.route('/dave')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    popular_movies = get_movies('popular')
    print('popular==>', popular_movies)
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title,popular = popular_movies)
    # return "lol"


@app.route('/movie/<movie_id>')
def movie(movie_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    title = f'You are viewing {movie_id}'
    return render_template('movie.html',title = title)