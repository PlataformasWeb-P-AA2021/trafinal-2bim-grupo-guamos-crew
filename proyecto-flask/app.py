from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='templates')


@app.route("/")
def hello_world():
    return "<p>Hola Mundo !</p>"


@app.route("/barrios")
def los_barrios():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/barrio/",
                     auth=('platweb', 'contigoPipo-234'))
    barrios = json.loads(r.content)
    return render_template("losbarrios.html", barrios=barrios)


@app.route("/persona")
def los_barrios():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/barrio/",
                     auth=('platweb', 'contigoPipo-234'))
    barrios = json.loads(r.content)
    return render_template("losbarrios.html", barrios=barrios)


@app.route("/casas")
def las_casas():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/casa/",
                     auth=('platweb', 'contigoPipo-234'))
    datos = json.loads(r.content)
    datos2 = []
    for d in datos:
        datos2.append({'prop_casa': obtener_persona(d['prop_casa']), 'direccion_casa': d['direccion_casa'],
                       'valor_casa': d['valor_casa'], 'color': d['color'],
                       'cuartos_casa': d['cuartos_casa'], 'pisos': d['pisos'],
                       'barrios': obtener_barrio(d['barrio'])})
    return render_template("lascasas.html", datos=datos2)


@app.route("/departamentos")
def los_departamentos():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/departamentos/",
                     auth=('platweb', 'contigoPipo-234'))
    datos = json.loads(r.content)
    datos2 = []
    for d in datos:
        datos2.append({'prop_dept': obtener_persona(d['prop_dept']), 'direccion_dept': d['direccion_dept'],
                       'valor_dept': d['valor_dept'], 'cuartos_dept': d['cuartos_dept'],
                       'mensualidad': d['mensualidad'], 'barrios': obtener_barrio(d['barrio'])})
    return render_template("losdepartamentos.html", datos=datos2)

# funciones ayuda

def obtener_barrio(url):
    """
    """
    r = requests.get(url, auth=('platweb', 'contigoPipo-234'))
    nombre_edificio = json.loads(r.content)['nombre']
    return nombre_edificio


def obtener_persona(url):
    """
    """
    r = requests.get(url, auth=('platweb', 'contigoPipo-234'))
    nombre_edificio = json.loads(r.content)['nombre']
    return nombre_edificio