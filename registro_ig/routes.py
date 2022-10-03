from flask import render_template
from registro_ig import app

@app.route("/")
def index():
    return render_template("index.html", pageTitle="Todos")