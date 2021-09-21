# las importaciones que hagan falta
from ListaAños import ListaAño
import os

class NodoAlumno:
    def __init__(self,carnet=0,dpi="",nombre="",carrera="",correo="",password="",creditos=0,edad=0,años = ListaAño):
        self.carnet = carnet 
        self.dpi = dpi  
        self.nombre = nombre
        self.carrera = carrera
        self.correo = correo
        self.password = password
        self.creditos = creditos
        self.edad = edad    
        self.años = años
        
        self.izq = None
        self.der = None
        self.altura=0

class AvlAlumno:
    def __init__(self) :
        self.raiz = None
    
    def insertar(self,dato):
        nuevo = NodoAlumno(carnet=dato)
        
        if self.raiz == None:
            self.raiz = nuevo
        else:
            #solo voy a insertar
            self.raiz = self.nodo_insertar(nuevo,self.raiz)
    
    def nodo_insertar(self,nuevo=NodoAlumno,raiz_actual=NodoAlumno):
       
        if raiz_actual != None:
            if raiz_actual.carnet > nuevo.carnet :
                
                raiz_actual.izq = self.nodo_insertar(nuevo,raiz_actual.izq)
                
                
            elif raiz_actual.carnet < nuevo.carnet:
                raiz_actual.der = self.nodo_insertar(nuevo,raiz_actual.der)
                
            
            
            return raiz_actual
    
        else:
            raiz_actual = nuevo
            return raiz_actual
        


    def graficar(self):
        cadena = "digraph arbol {\n"
        if(self.raiz != None):
            cadena += self.listar(self.raiz)
            cadena += "\n"
            cadena += self.enlazar(self.raiz)
        cadena += "}"
        Archivo = open("ejemplo.dot","w+")
        Archivo.write(cadena)
        Archivo.close()

    def listar(self, raiz_actual):
        if raiz_actual:
            cadena = "n"+str(raiz_actual.carnet)+"[label= \""+str(raiz_actual.carnet)+"\"];\n"
            cadena += self.listar(raiz_actual.izq)
            cadena += self.listar(raiz_actual.der)
            return cadena
        else:
            return ""
    
    def enlazar(self,raiz_actual):
        cadena =""
        if raiz_actual:
            if raiz_actual.izq:
                cadena+= "n"+str(raiz_actual.carnet)+" -> n"+str(raiz_actual.izq.carnet)+"\n"
            if raiz_actual.der:
                cadena+= "n"+str(raiz_actual.carnet)+" -> n"+str(raiz_actual.der.carnet)+"\n"

            cadena += self.enlazar(raiz_actual.izq)
            cadena += self.enlazar(raiz_actual.der)
        
        return cadena

arbol = AvlAlumno()

arbol.insertar(dato=10)
arbol.insertar(dato=15)
arbol.insertar(dato=5)
arbol.insertar(dato=1)
arbol.insertar(dato=16)

arbol.graficar()

#dejamos aqui, volvamos este arbol en un avl todo esta bien en la insercion. 

    