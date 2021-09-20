#por si se necesitan hacer importaciones




class nodoTT:
    def __init__(self,carne,nombre,descrip,materia,fecha,hora,estado):
        self.carne = carne
        self.nombre = nombre
        self.descripcion = descrip
        self.materia = materia
        self.fecha = fecha
        self.hora = hora
        self.estado= estado
        self.anterior = None
        self.siguiente = None
        #creacion de nodo para la lista de tareas
        
class listaT:
    def __init__(self):
        self.inicio = None
        self.fin= None
        self.tamaño = 0
    #creacion de la lista doble
    #metodos para la lista
    
    def insertar(self,carne,nombre,descrip,materia,fecha,hora,estado ):
        nuevo = nodoTT(carne,nombre,descrip,materia,fecha,hora,estado)
        
        if self.inicio == None:
            self.inicio = nuevo
            self.fin = nuevo
            self.tamaño = self.tamaño+1
            
            
        else:
            nuevo.anterior = self.fin
            self.fin.siguiente = nuevo
            self.fin = nuevo
            
            self.tamaño = self.tamaño+1
            
    #insercion
    
    def buscarT(self,nombre,descrip,estado):
        pivote = self.inicio
        if pivote:
            for n in self.tamaño:
                if pivote.nombre == nombre:
                    if pivote.descripcion == descrip:
                        if pivote.estado == estado:
                            print("si existe",end="")
                        
                        else:
                            print("el estado no coincide")
                    
                    else:
                        print("la descripcion no coincide")    
                    #entra
                else:
                    print("Nombre no coincide ")
            
            pivote = pivote.siguiente
    
    #termina la busqueda
    def MostarT(self):
        pivote = self.inicio
        print(f"tamaño = {self.tamaño}")
        
        while pivote != None:
            print(pivote.nombre," -> ", end="")
            pivote = pivote.siguiente
        
    #mostramos
    
                            
                    
                 
                    
        
            
            
        

    

        