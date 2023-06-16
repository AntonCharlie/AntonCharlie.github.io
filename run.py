# file input
from flask import Flask, render_template

# create flask
app = Flask(__name__)

# route
@app.route("/")
@app.route("/home")
def home():
    return render_template('main.html')

# @app.route("/about")
# def about():
#     return render_template("about.html")

# @app.route("/gallery")
# def intro():
#     return render_template("character.html")

# @app.route("/register")
# def register():
#     return render_template("register.html")

# @app.route("/login")
# def login():
#     return render_template("login.html")

# @app.route("/preview")
# def preview():
#     return render_template("preview.html")

#trigger
if __name__ == "__main__":
    app.run(debug=True)