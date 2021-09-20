from flask import Flask
from flask import request
from Estructuras.ListaTareas import listaT
import os

app = Flask(__name__)
#aqui la dejamos seguimos haciendo los endpoints 
@app.route('/') #decorador
def index():
    return '<h1> Cambio. <h1>'

@app.route('/') #decorador
def index():
    return '<h1> Cambio. <h1>'
if __name__=='__main__':
# app.run(debug= True, port=3000)
    
    lista = listaT()
    lista.insertar("201314881","Juan","Tarea loca","EDD","14/10/1994","12:00","completa")
    lista.insertar("201314881","Pablo","Tarea loca","EDD","14/10/1994","12:00","completa")
    lista.insertar("201314881","orellana","Tarea loca","EDD","14/10/1994","12:00","completa")
    lista.insertar("201314881","penate","Tarea loca","EDD","14/10/1994","12:00","completa")
    lista.MostarT()
    
    

