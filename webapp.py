from flask import Flask, request, render_template, flash
from markupsafe import Markup
from datetime import datetime

import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')
    
@app.route('/recommender')
def render_recommender():
    with open('video_games.json') as video_games_data:
        games = json.load(video_games_data)
    if 'genre' in request.args:
        genre = request.args['genre']
        return render_template('recommenderdata.html', options=get_genre_options(games), genre=genre)
    return render_template('recommender.html', options=get_genre_options(games))

@app.route("/consolechart")
def render_consolechart():
    return render_template('consolechart.html')
    
def get_genre_options(games):
    genres = []
    options = ""
    for g in games:
        genre = g["Metadata"]["Genres"]
        if (genre not in genres):
            genres.append(genre)
            options += Markup("<option value=\"" + str(genre) + "\">" + str(genre) + "</option>")
    return options    

def is_localhost():
    root_url = request.url_root
    developer_url = 'http://127.0.0.1:5000/'
    return root_url == developer_url
    
if __name__=="__main__":
    app.run(debug=True)
