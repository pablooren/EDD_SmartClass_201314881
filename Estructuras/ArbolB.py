from listaB import Lista_NodoB
from PaginaB import Pagina
from NodoB import NodoB

class ArbolB:
    def __init__(self):
        self.raiz = None
        self.orden = 5
        self.altura =0
        
    def GetAltura(self):
        return self.altura
    
    def InsertarNodo(self,codigo,nombre):
        nuevo = NodoB(codigo=codigo,nombre=nombre,creditos=125,requisitos="112,114",obligatorio=True)
        
        if self.raiz == None:
            list1 = Lista_NodoB()
            
            self.raiz = Pagina(list1)
            self.raiz.raiz = True
            self.raiz = self.raiz.Insertar_Pag(nuevo)
            print("lo insertamos")
        else:
            if self.altura ==0:#esto es porque no se ha dividido la raiz
                respuesta = self.raiz.Insertar_Pag(nuevo)
                
                if isinstance(respuesta, Pagina):
                    self.raiz = respuesta
                    print("se inserto")
                elif isinstance(respuesta,NodoB):
                    self.altura = self.altura+1
                    list2 = Lista_NodoB()
                    self.raiz = Pagina(list2)
                    self.raiz = self.raiz.Insertar_Pag(nuevo)
                
            else: #esto es porque la raiz ya se dividio
                respuesta = insertar_recorrer(nuevo,self.raiz)
                
                if isinstance(respuesta,NodoB):
                    self.altura = self.altura+1
                    list3 = Lista_NodoB
                    self.raiz  = Pagina(list3)
                    self.raiz = self.raiz.Insertar_Pag(respuesta)
                else:
                    self.raiz = respuesta
    
    
    def insertar_recorrer(self,nuevo,raiz):
        
        
        if raiz.Es_Hoja(raiz):
            respuesta = raiz.Insertar_Pag(nuevo)
            return respuesta
        
        else:
            if nuevo.codigo < raiz.claves.GetPrimero().codigo :
                respuesta = insertar_recorrer(nuevo,raiz.claves.GetPrimero().izq)
                
                if isinstance(respuesta, NodoB):
                    return raiz.Insertar_Pag(respuesta)
                else:
                    raiz.claves.getPrimero().izq = respuesta
                    return raiz
                
            elif nuevo.codigo > raiz.claves.GetUltimo().codigo:
                respuesta = insertar_recorrer(nuevo,raiz.claves.GetUltimo().der)
                
                if isinstance(respuesta, NodoB):
                    return raiz.Insertar_Pag(respuesta)
                
                else:
                    raiz.claves.GetUltimo().der = respuesta
                    return raiz
            
            else:
                pivote = raiz.claves.GetPrimero()
                
                while pivote != None:
                    if nuevo.codigo < pivote.codigo:
                        respuesta = insertar_recorrer(nuevo,pivote.izq)
                        
                        if isinstance(respuesta, NodoB):
                            return raiz.Insertar_Pag(respuesta)
                        else:
                            pivote.izq = respuesta
                            pivote.anterior.der = respuesta
                            return raiz
                        
                    elif nuevo.codigo == pivote.codigo:
                        return raiz
                    else:
                        pivote = pivote.siguiente
        return self
    
    
    #aqui va lo de graficar el arbol b
    
    #empecemos a ver la conexion de EDD's 
         
                      
            
            
