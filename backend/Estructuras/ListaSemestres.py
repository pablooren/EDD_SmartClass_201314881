# Aqui nos falta crear el arbol B para los cursos que se asignen


class NodoSemestre:
    def __init__(self, nombre, cursos ):
        self.nombre = nombre
        self.cursos = cursos
        
        self.anterior = None
        self.siguiente = None
        #creacion de nodo de meses
    
class ListaSemestre:
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.tamaño =0
    #creacion de la lista doble enlazada de meses
    
    def insertar(self,nombre,cursos):
        nuevo = NodoSemestre(nombre,cursos)
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
    
    