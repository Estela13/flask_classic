from distutils.log import error
from flask import render_template, request, redirect, url_for
from registro_ig import app
from registro_ig.models import select_all, insert
from datetime import date

@app.route("/")
def index():
    # consultar todos los movimientos de la BASE DE DATOS
    registros = select_all()
    return render_template("index.html", pageTitle="Todos", data=registros)


def validaFormulario(camposFormulario):
    errores = []
    hoy = date.today().isoformat()
    if camposFormulario['date'] > hoy:
        errores.append("La fecha introducida es el futuro.")

    if camposFormulario['concept'] == "":
        errores.append("Introduce un concepto para la transacción.")

    #La primera condición es para que el número sea distinto de cero
    #la segunda condición es para que el campo no esté vacío
    if camposFormulario["quantity"] == "" or float(camposFormulario["quantity"]) == 0.0:
        errores.append("Introduce una cantidad positiva o negativa.")

    return errores



@app.route("/new", methods=["GET", "POST"])
def new():
    if request.method == "GET":
        return render_template("new.html", dataForm=None)
    else:
        errores = validaFormulario(request.form)
        if not errores:
            insert([request.form['date'],
                    request.form['concept'],
                    request.form['quantity']
                  ])
            return redirect(url_for("index"))


        else:
            return render_template("new.html", dataForm=request.form, msgErrors=errores)
