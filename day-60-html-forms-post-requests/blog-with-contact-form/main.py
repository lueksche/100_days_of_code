from flask import Flask, render_template, request
import requests
import smtplib

MY_EMAIL = "lukassmtptest@gmail.com"
PASSWORD = "khcx tvji fywp jjik"

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(MY_EMAIL, MY_EMAIL, email_message)

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/form-entry", methods=['POST'])
def receive_data(name, email, phone, message):
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']
    message = email+"\n"+phone+"\n\n"+message
    send_email(name, email, phone, message)
    return "<h1>Successfully sent your message</h1>"

if __name__ == "__main__":
    app.run(debug=True, port=5001)
 