from flask import Flask, render_template
from datetime import datetime
import requests
import json

URL_AGIFY = "https://api.agify.io"
URL_GENDERIZE = "https://api.genderize.io"
CURRENT_YEAR = datetime.today().year
NAME = "Lukas Deibel"

app = Flask(__name__)

def get_age(name):
    response = requests.get(url=URL_AGIFY+"?name="+name)
    data = json.loads(response.content)
    age = data['age']
    return age

def get_gender(name):
    response = requests.get(url=URL_GENDERIZE+"?name="+name)
    data = json.loads(response.content)
    gender = data["gender"]
    return gender


@app.route('/')
def home():
    return render_template("index.html", YEAR=CURRENT_YEAR, NAME=NAME)

@app.route('/guess/<username>')
def guess(username):
    username = str.title(username)
    age = get_age(username)
    gender = get_gender(username)
    return render_template("guess.html", YEAR=CURRENT_YEAR, NAME=NAME, USERNAME=username, GENDER=gender, AGE=age)

if __name__ == "__main__":
    app.run(debug=True)


