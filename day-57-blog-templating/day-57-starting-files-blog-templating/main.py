from flask import Flask, render_template
import requests

URL = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(URL)
all_posts = response.json()

app = Flask(__name__)

@app.route('/')
def home(all_posts):
    return render_template("index.html", posts=all_posts)

@app.route('/blog/<int:num>')
def get_blog(all_posts, num):
    return render_template("post.html", posts=all_posts, num=num)

if __name__ == "__main__": 
    app.run(debug=True)
