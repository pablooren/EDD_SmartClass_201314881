from flask import Flask
from flask import request
from Estructuras.ListaTareas import listaT
import os

app = Flask(__name__)
#aqui la dejamos seguimos haciendo los endpoints 
@app.route('/') #decorador
def index():
    return '<h1> Cambio. <h1>'


app.run(debug= True, port=3000)

    
    

