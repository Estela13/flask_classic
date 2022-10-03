from flask import render_template
from registro_ig import app
from registro_ig.models import select_all

@app.route("/")
def index():
    # consultar todos los movimientos de la BASE DE DATOS
    registros = select_all()
    return render_template("index.html", pageTitle="Todos", data=registros)
    