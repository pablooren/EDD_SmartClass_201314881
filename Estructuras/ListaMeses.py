from PrincipalTareas import Matriz_ortogonal
class NodoMes:
    def __init__(self, nombre, tareas = Matriz_ortogonal ):
        self.nombre = nombre
        self.tareas = tareas
        self.anterior = None
        self.siguiente = None
        #creacion de nodo de meses
    
class ListaMes:
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.tamaño =0
    #creacion de la lista doble enlazada de meses
    
    def insertar(self,nombre,tareas):
        nuevo = NodoMes(nombre,tareas)
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
    
    
    
        