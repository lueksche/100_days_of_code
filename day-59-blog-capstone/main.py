from flask import Flask, render_template
import requests

app = Flask(__name__)

API_BLOGPOSTS = "https://api.npoint.io/5d4f458c2c6d6f487f3f"

response = requests.get(API_BLOGPOSTS)
all_posts = response.json()

@app.route('/')
def index():
    return render_template('index.html', posts=all_posts)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in all_posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == '__main__':
    app.run(debug=True)
