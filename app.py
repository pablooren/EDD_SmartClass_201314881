from flask import Flask, json
from flask import request
from flask import jsonify
from flask import request
from Estructuras.ListaAños import ListaAño
from Estructuras.ListaMeses import ListaMes
from Estructuras.ListaSemestres import ListaSemestre
from Estructuras.ListaTareas import listaT, nodoTT
from Estructuras.MatrizTareas import Matriz_ortogonal
from carga_masiva import carga_masiva
from lectura_json import lectura_json
from Estructuras.ArbolB import ArbolB
import os

from Estructuras.AvlAlumnos import AvlAlumno


#Desde aqui iniciamos con las estructuras
Estudiantes = AvlAlumno()
Estu = AvlAlumno()
Pensum = ArbolB()


recor = listaT()
recor.insertar("201314881","Mate Intermedia 1","Tarea de matematica inter 10","Matematica Intermedia 1","13/10/2020","8:00","incompleto")
Estudiantes.insertar("201314881","2568861992101","Pablo Orellana","ciencias y sistemas","pablooren@gmail","123456asdf","130","26")
Estudiantes.raiz.años = ListaAño()
meses = ListaMes()
matriz = Matriz_ortogonal()
tareas = listaT()

matriz.insertar(13,10,recor)
matriz.insertar(13,11,recor)
matriz.insertar(12,10,recor)

meses.insertar("10",matriz)
Estudiantes.raiz.años.insertar("2020",meses,ListaSemestre())






app = Flask(__name__)
#aqui la dejamos seguimos haciendo los endpoints 
@app.route('/') #decorador
def index():
    return 'Salida valida'

#Endopoints de estudiante
@app.route('/estudiante', methods=['GET'])
def get_estudiante():
    datos = request.json
    lc = lectura_json()
    res = lc.GetAlumno(datos,Estudiantes)
    Estudiantes.graficar()
    
    return res

@app.route('/estudiante', methods=['POST'])
def post_estudiante():
    datos = request.json
    lc = lectura_json()
    
    res =lc.postAlumno(datos,Estudiantes)
    Estudiantes.graficar()
    return jsonify(res)
    
    

@app.route('/estudiante', methods=['PUT'])
def put_estudiante():
    datos = request.json
    lc = lectura_json()
    res = lc.UpAlumno(datos,Estudiantes)
    Estudiantes.graficar()
    return res
 
@app.route('/estudiante', methods=['DELETE'])
def delete_estudiante():
    datos = request.json
    lc = lectura_json()
    
    
    return 'salida delete'




@app.route('/recordatorios', methods=['GET'])
def get_recordatorios():
    datos = request.json
    
    return jsonify(datos)

@app.route('/recordatorios', methods=['POST'])
def post_recordatorios():
    return 'salida del post'

@app.route('/recordatorios', methods=['PUT'])
def put_recordatorios():
    return 'salida put'

@app.route('/recordatorios', methods=['DELETE'])
def delete_recordatorios():
    return 'salida delete'




#endpoints de recordatorios


@app.route('/cursosEstudiante', methods=['POST'])
def post_cursosEstudiante():
    datos = request.json
    
    return jsonify(datos)

@app.route('/cursosPensum', methods=['POST'])
def post_cursosPensum():
    return 'salida del post'

# endpoints de carga y reportes

@app.route('/carga', methods=['POST'])
def get_carga():
    #estudiante|cursoPensum|CursosEstudiante
    #C:\\Users\\pablo\\Desktop\\Entrada\\Estudiantes.txt
    datos = request.json
    if datos['tipo'] == "estudiante":
        Carga_MasivaE(datos['path'])
    
    elif datos['tipo']  == "cursoPensum":
        Carga_MasivacP(datos['path'])
    
    elif datos['tipo'] == "CursosEstudiante":
        Carga_MasivacE(datos['path'])
    else:
        return jsonify('opcion invalida')
        
    
    return jsonify('.')


def Carga_MasivaE(ruta):
    f = open(ruta,'r',encoding="utf-8")
    mensaje = f.read()
    f.close()
    carga = carga_masiva()
    carga.Ingresar_estudiante(mensaje,Estudiantes)
    Estudiantes.graficar()
  #  carga.Ingresar_recordatorio(mensaje,)
    carga.AsignarRe(Estudiantes)
    

def Carga_MasivacP(ruta):
    lc = lectura_json()
    
    lc.CursosPensum(ruta,Pensum)
    Pensum.GraficarArbol()
    



def Carga_MasivacE(ruta):
    pass

@app.route('/reporte', methods=['GET'])
def get_reporte():
    datos = request.json
    if datos['tipo'] == 0:
        Estudiantes.graficar()
        
    
    if datos['tipo'] == 3:
        Pensum.GraficarArbol()
        



if __name__ == "__main__":
    
    app.run(debug= True, port=3000)

    




