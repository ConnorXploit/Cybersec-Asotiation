from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def recogerDatos():
    r = requests.get('http://opendata.euskadi.eus/contenidos/ds_eventos/agenda_cultura_euskadi/es_kultura/adjuntos/kulturklik.json')
    if r.status_code == 200:
        return r.text.replace('jsonCallback', '')
    else:
        print('Algo ha ido mal')
        return ''

@app.route("/")
def edad():
    datos = recogerDatos()
    return render_template('index.html', datos=datos)

if __name__ == "__main__":
    app.run(threaded=True, debug=True)