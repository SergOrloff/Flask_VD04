from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def company():
    return render_template("index.html")


@app.route("/person/")
def person():
    return render_template("blog.html")

@app.route("/contacts/")
def contacts():
    return render_template("contacts.html")

if __name__ == "__main__":
    app.run()