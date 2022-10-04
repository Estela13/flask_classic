import sqlite3
from config import ORIGIN_DATA

def filas_to_diccionario(filas, columnas):
    resultado = []
    for fila in filas:
        posicion_columna = 0
        d = {}
        for campo in columnas:
            d[campo[0]] = fila[posicion_columna]
        d = {}
        for campo in columnas:
            d[campo[0]] = fila[posicion_columna]
            posicion_columna += 1
        resultado.append(d)

    """
    for fila in filas:
        d = {}
        for posicion, campo in enumerate(columnas):
            d[campo[0]] = fila[posicion]
        resultado.append(d)
    """
    return resultado

def delete_by(id):
    conn = sqlite3.connect(ORIGIN_DATA)
    cur = conn.cursor()

    cur.execute("DELETE FROM movements WHERE id = ?", (id,))

    conn.commit()
    conn.close()

def select_by(id):
    conn = sqlite3.connect(ORIGIN_DATA)
    cur = conn.cursor()

    cur.execute("SELECT id, date, concept, quantity from movements WHERE id = ?", (id,))

    resultado = filas_to_diccionario(cur.fetchall(), cur.description)

    conn.close()

    if resultado:
        return resultado[0]
    return {}




def select_all():
    conn = sqlite3.connect(ORIGIN_DATA)
    cur = conn.cursor()

    cur.execute("SELECT id, date, concept, quantity from movements order by date;")

    resultado = filas_to_diccionario(cur.fetchall(), cur.description)

    conn.close()

    return resultado

def insert(registro):
    """
    INSERT INTO movements (date, concept, quantity) values (?, ?, ?)
    params:     cur.execute("INSERT INTO movements (date, concept, quantity) values (?, ?, ?)", ['2022-04-08', 'Cumple', -80])
    conn.commit() antes de hacer el conn.close()
    """
    conn = sqlite3.connect(ORIGIN_DATA)
    cur = conn.cursor()
    cur.execute("INSERT INTO movements (date, concept, quantity) values (?, ?, ?);", registro)
    conn.commit()
    conn.close()