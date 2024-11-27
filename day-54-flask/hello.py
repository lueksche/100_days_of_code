from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
@make_emphasis
def say_bye():
    return "<p>Bye!</p>"

@app.route("/username/<name>/<int:number>")
def greet_user(name, number):
    return f"<p>Hello there, {name}. You are {number} old!</p>"

if __name__ == "__main__":
    app.run(debug=True)