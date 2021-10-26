import json

from flask.json import jsonify

from Estructuras.AvlAlumnos import AvlAlumno, NodoAlumno

class lectura_json():
    def __init__(self):
        pass
    
    def cargar(self):
        ruta = 'prueba.json'
        with open(ruta) as contenido:
            Cursos = json.load(contenido)
            for curso in Cursos['Estudiantes']:
                print (curso.get('Carnet'))
                for anios in curso['Anios']:
                    print(" ",anios.get('Anio'))
                    for semestre in anios['Semestres']:
                        print("     ", semestre.get('Semestre'))
                        for cursos in semestre['Cursos']:
                            print("         ", cursos)
    
    def guardar(self):
        pass
    
    def postAlumno(self,datos,avl):
        print(datos.get('carnet'))
        avl.insertar(datos.get('carnet'),datos.get('DPI'),datos.get('nombre'),datos.get('carrera'),datos.get('correo'),datos.get('password'),datos.get('creditos'),datos.get('edad'))
        return "alumno ingresado"  
    
    def UpAlumno(self,datos,avl):
        pivote = avl.Buscar(datos.get('carnet'),avl.raiz)
       # pivote = NodoAlumno()
        if pivote != None:
            pivote.nombre = datos.get('nombre')
            pivote.dpi = datos.get('dpi')
            pivote.carrera = datos.get('carrera')
            pivote.correo = datos.get('correo')
            pivote.password = datos.get('password')
            pivote.creditos = datos.get('creditos')
            pivote.edad = datos.get('edad')
            return "Cambio realizado con exito"
        
        else:
            return "Carnet no existe"    
    
    def GetAlumno(self,datos,avl):
        pivote = avl.Buscar(datos.get('carnet'),avl.raiz)
      #  pivote = NodoAlumno()
        if pivote != None:
            data = {}
            
            data['Estudiante'] =[]
            data['Estudiante'].append({
                'carnet': pivote.carnet ,
                'DPI': pivote.dpi,
                'Nombre': pivote.nombre,
                'Carrera': pivote.carrera,
                'Correo': pivote.correo,
                'Password': pivote.password,
                'Creditos': pivote.creditos,
                'Edad': pivote.edad
                
            })
            
            return jsonify(data)
        else:
            return jsonify("Carnet no existe")   
    
    def ElimAlumno(self,raiz,nn,dato):
         if raiz:
             if raiz.carnet != dato:
                 
                self.ElimAlumno(raiz.izq,nn,dato)
                nn.insertar(raiz.carnet,raiz.dpi,raiz.nombre,raiz.carrera,raiz.correo,raiz.password,raiz.creditos,raiz.edad)
                self.ElimAlumno(raiz.izq,nn,dato)
        
          

    def CursosPensum(self, ruta,B):
        with open(ruta) as contenido:
            Cursos = json.load(contenido)
            for curso in Cursos['Cursos']:
                B.InsertarNodo(curso.get('Codigo'),curso.get('Nombre'),curso.get('Creditos'),curso.get('Prerequisitos'),curso.get('Obligatorio'))
               
        
    def ElimAlum(self,Avl,dato):
        pi = Avl
        nn = AvlAlumno()
        self.ElimAlumno(pi.raiz,nn,dato)
        return nn
    
            
           
        
        
             
                


carga = lectura_json()
carga.cargar()
