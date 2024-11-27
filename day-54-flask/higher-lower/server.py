from flask import Flask
from random import randint

high = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"

low = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"

correct = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"

app = Flask(__name__)

def check_guess(*args):
    if args[0] > args[1]:
        return  f"<h1 style='color: red'>Too low, try again!</h1>" \
                f"<img src='{low}'>"
    elif args[0] < args[1]:
        return  f"<h1 style='color: purple'>Too high, try again!</h1>" \
                f"<img src='{high}'>"
    else:
        return  f"<h1 style='color: green'>You found me!</h1>" \
                f"<img src='{correct}'>"

def get_random_number():
    return randint(0, 9)

@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route('/<int:guess>')
def guess_number(guess):
    random_number = get_random_number()
    return check_guess(random_number, guess)

if __name__ == "__main__":
    app.run(debug=True)