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
        
            self.raiz = self.nodo_insertar(nuevo,self.raiz)
    
    def nodo_insertar(self,nuevo,raiz_actual):
        if raiz_actual:
            if raiz_actual.carnet   > nuevo.carnet:
                raiz_actual.izq = self.nodo_insertar(nuevo,raiz_actual.izq)
                #validar si necesita rotacion
                if (self.altura(raiz_actual.der)-self.altura(raiz_actual.izq)== -2):
                    if nuevo.carnet < raiz_actual.izq.carnet:
                        raiz_actual = self.R_izq(raiz_actual)
                    else:
                        raiz_actual = self.R_izq_der(raiz_actual)

            elif raiz_actual.carnet < nuevo.carnet:
                raiz_actual.der = self.nodo_insertar(nuevo,raiz_actual.der)
                #validar si necesita rotacion
                if (self.altura(raiz_actual.der)-self.altura(raiz_actual.izq)== 2):
                    if nuevo.carnet > raiz_actual.der.carnet:
                        raiz_actual = self.R_der(raiz_actual)
                    else:
                        raiz_actual = self.R_der_izq(raiz_actual)

            #calcular nueva altura
            raiz_actual.altura = self.max(self.altura(raiz_actual.der),self.altura(raiz_actual.izq)) + 1
            return raiz_actual
        else:
            raiz_actual = nuevo
            return raiz_actual
    def max(self, v1, v2):
        if v1> v2:
            return v1
        else:
            return v2

    def altura(self, nodo):
        if nodo:
            return nodo.altura
        else:
            return -1


    #ROTACIONES
    #SIMPLE IZQ 
    def R_izq(self, nodo):
        aux = nodo.izq
        nodo.izq = aux.der
        aux.der = nodo
        nodo.altura = self.max(self.altura(nodo.der), self.altura(nodo.izq)) +1
        aux.altura = self.max(nodo.altura, self.altura(nodo.izq)) +1
        return aux

    #SIMPLE DER
    def R_der(self, nodo):
        aux = nodo.der
        nodo.der = aux.izq
        aux.izq = nodo
        nodo.altura = self.max(self.altura(nodo.der), self.altura(nodo.izq)) +1
        aux.altura = self.max(nodo.altura, self.altura(nodo.der)) +1
        return aux

    #IZQ-DER
    def R_izq_der(self, nodo):
        nodo.izq = self.R_der(nodo.izq)
        aux = self.R_izq(nodo)
        return aux

    #DER-IZQ
    def R_der_izq(self, nodo):
        nodo.der = self.R_izq(nodo.der)
        aux = self.R_der(nodo)
        return aux

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








    