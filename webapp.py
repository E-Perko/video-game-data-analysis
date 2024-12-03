from flask import Flask, request, render_template, flash
from markupsafe import Markup
from datetime import datetime
import random

import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')
    
"""@app.route('/recommender')
def render_recommender():
    with open('video_games.json') as video_games_data:
        games = json.load(video_games_data)
    if 'genre' in request.args:
        genre = request.args['genre']
        return render_template('recommenderdata.html', options=get_genre_options(games), genre_list=genres)
    else:
        return render_template('recommender.html', options=get_genre_options(games))"""

@app.route('/recommender')
def render_recommender():
    with open('video_games.json') as video_games_data:
        games = json.load(video_games_data)
    if 'genre' in request.args:
        genre = request.args['genre']
    if 'console' in request.args:
        console = request.args['genre']
    return render_template('recommender.html', genre_options=get_genre_options(games), console_options=get_console_options(games))

@app.route("/consolechart")
def render_consolechart():
    with open('video_games.json') as video_games_data:
        games = json.load(video_games_data)
    return render_template('consolechart.html', points=console_game_totals(games))

def get_genre_options(games):
    genres = []
    genre_options = ""
    for g in games:
        genre = g["Metadata"]["Genres"]
        if (genre not in genres):
            genres.append(genre)
            genre_options += Markup("<option value=\"" + str(genre) + "\">" + str(genre) + "</option>")
    return genre_options

def get_console_options(games):
    consoles = []
    console_options = ""
    for g in games:
        console = g["Release"]["Console"]
        if (console not in consoles):
            console.append(console)
            console_options += Markup("<option value=\"" + str(console) + "\">" + str(console) + "</option>")
    return console_options    

def console_game_totals(games):
    consoles = {}
    for g in games:
        console = g["Release"]["Console"]
        if console in consoles:
            consoles[console] = consoles[console] + 1
        else:
            consoles[console] = 1
    graph_points = ""
    for console, video_games in consoles.items():
        graph_points = graph_points + Markup("{ label: '" + str(console) + "', y: " + str(video_games) + " }, ")
    graph_points = graph_points[:-2]
    return graph_points

"""foo = ['a', 'b', 'c', 'd', 'e']
print(random.choice(foo))"""    
    
def is_localhost():
    root_url = request.url_root
    developer_url = 'http://127.0.0.1:5000/'
    return root_url == developer_url
    
if __name__=="__main__":
    app.run(debug=True)
