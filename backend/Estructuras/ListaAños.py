from Estructuras.ListaMeses import ListaMes
from Estructuras.ListaSemestres import ListaSemestre
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
    def tam(self):
        return self.tamaño
    
    def insertar(self,nombre,meses, semestres):
        nuevo = NodoAño(nombre,meses=ListaMes(),semestres=ListaSemestre())
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
        while pivote != None:
            print(pivote.nombre," -> ", end="")
            pivote = pivote.siguiente
    #Metodo de mostrar
    
    def Buscar(self,dato):
        pivote = self.inicio
        while pivote != None:
            if dato == pivote.nombre:
                return pivote
            else:
                pivote = pivote.siguiente

        return None
    