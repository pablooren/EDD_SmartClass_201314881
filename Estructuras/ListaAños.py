from ListaMeses import ListaMes
from ListaSemestres import ListaSemestre
class NodoAño:
    def __init__(self, nombre, meses = ListaMes, semestres = ListaSemestre ):
        self.nombre = nombre
        self.meses = meses
        self.semestres = semestres
        
        self.anterior = None
        self.siguiente = None
        #creacion de nodo de meses
    
class ListaAño:
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.tamaño =0
    #creacion de la lista doble enlazada de meses
    
    def insertar(self,nombre,meses, semestres):
        nuevo = NodoAño(nombre,meses,semestres)
        if self.inicio == None:
            self.inicio = nuevo
            self.fin = nuevo
            self.tamaño = self.tamaño+1
        else:
            nuevo.anterior = self.fin
            self.fin.siguiente = nuevo
            self.fin = nuevo
            
            self.tamaño = self.tamaño+1
    #Metodo de insercion 
    
    def Mostrar(self):
        pivote = self.inicio
        print(f"tamaño = {self.tamaño}")
        
        while pivote != None:
            print(pivote.nombre," -> ", end="")
            pivote = pivote.siguiente
    #Metodo de mostrar
    
    