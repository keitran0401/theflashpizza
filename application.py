from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/menu')
def menu():
    return render_template("menu.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/signin')
def signin():
    return render_template("signin.html")


@app.route('/register', methods=["POST"])
def register():
    return render_template("success.html")


if __name__ == '__main__':
    app.run()
