from flask import Flask, url_for, render_template
from markupsafe import Markup
from datetime import datetime

import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')

def is_localhost():
    root_url = request.url_root
    developer_url = 'http://127.0.0.1:5000/'
    return root_url == developer_url
    
if __name__=="__main__":
    app.run(debug=False)
