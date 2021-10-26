
from Estructuras.NodoB import NodoB

class Lista_NodoB:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamaño = 0
        
    def GetTamaño(self):
        return self.tamaño
    
    def GetPrimero(self):
        return self.primero
    
    def GetUltimo(self):
        return self.ultimo
    
    def Insertar(self, Nodob):
        nuevo = Nodob
        
        
        if self.primero == None: #es el primero que insertamos
            self.primero = nuevo
            self.ultimo = nuevo
            self.tamaño = self.tamaño+1
          #  print("se inserto el primer nodo de la hoja")
            
        else:
            if self.primero == self.ultimo: #es el segundo que insertamos
                if nuevo.codigo < self.primero.codigo:
                    nuevo.siguiente =self.primero
                    self.primero.anterior =nuevo
                    self.primero.izq = nuevo.der
                    self.primero = nuevo
                    self.tamaño = self.tamaño+1
                   # print("se inserto segundo nodo de la hoja")
                
                elif nuevo.codigo > self.primero.codigo:
                    self.ultimo.siguiente = nuevo
                    nuevo.anterior = self.ultimo
                    self.ultimo.der = nuevo.izq
                    self.ultimo = nuevo
                    self.tamaño = self.tamaño+1
                  #  print("se inserto segundo nodo de la hoja")
                
                else:
                    print ("ya un curso con el mismo codigo")
                    return None
               
            else: #insertamos del 3ro en adelante
                
                if nuevo.codigo < self.primero.codigo:
                    nuevo.siguiente = self.primero
                    self.primero.anterior = nuevo
                    self.primero.izq = nuevo.der
                    self.primero = nuevo
                    self.tamaño = self.tamaño+1
                                      
                elif nuevo.codigo > self.ultimo.codigo:
                    self.ultimo.siguiente = nuevo
                    nuevo.anterior = self.ultimo
                    self.ultimo.der  = nuevo.izq
                    self.ultimo  = nuevo
                    self.tamaño = self.tamaño+1
                    
                
                else :
                    pivote = self.primero
                    
                    while pivote != None:
                        if nuevo.codigo < pivote.codigo:
                            nuevo.siguiente = pivote
                            nuevo.anterior = pivote.anterior
                            
                            pivote.izq = nuevo.der
                            pivote.anterior.der = nuevo.izq
                            
                            pivote.anterior.siguiente = nuevo
                            pivote.anterior = nuevo
                            self.tamaño = self.tamaño+1
                            
                            
                            break
                            
                        
                        elif nuevo.codigo == pivote.codigo:
                            print ("Ya hay un codigo con este curso")
                            return None
                        else:
                            pivote = pivote.siguiente
                          #  print ("pasa ahora pivote es ",pivote.codigo )
    
    
    def recorrer(self):
        pivote = self.primero
        
        while pivote != None:
            print (pivote.codigo, " / ", pivote.nombre , " ---")
            
            pivote = pivote.siguiente
            
    def Eliminar(self, codigo):
        pivote = self.primero
        
        while pivote != None:
            if pivote.codigo == codigo:
                break
            else:
                pivote = pivote.siguiente
        
        if pivote != None:
            if self.primero == self.ultimo:
                if pivote == self.primero:
                    self.primero = None
                    self.ultimo = None
            else:
                if pivote == self.primero:
                    self.primero = pivote.siguiente
                    self.primero.anterior = None
                
                elif pivote == self.ultimo:
                    self.ultimo = pivote.anterior
                    self.ultimo.siguiente = None
                
                else:
                    pivote.anterior.siguiente = pivote.siguiente
                    pivote.siguiente.anterior = pivote.anterior
                    pivote.siguiente = None
                    pivote.anterior = None
        else:
            print("el codigo no existe") 
    
    



                  
                



                        
                        
                
                    
                
            
            
            