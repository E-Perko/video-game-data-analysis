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
    if 'genres' in request.args:
        genres = request.args['genres']
        return render_template('recommenderdata.html', options=get_year_options(games), genres=genres)
    return render_template('recommender.html', options=get_genres_options(games))

def get_genres_options(weeks):
    """Returns the html code for a drop down menu.  Each option is a year for which there is complete data (1990 and 2016 are missing data)."""
    genres = []
    options = ""
    for w in weeks:
        genres = w["Metadata"]["Genres"]
        if (genres not in genres):
            years.append(genres)
            options += Markup("<option value=\"" + str(genres) + "\">" + str(genres) + "</option>")
    return options    

def is_localhost():
    root_url = request.url_root
    developer_url = 'http://127.0.0.1:5000/'
    return root_url == developer_url
    
if __name__=="__main__":
    app.run(debug=False)
