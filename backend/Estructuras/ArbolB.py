from Estructuras.listaB import Lista_NodoB
from Estructuras.PaginaB import Pagina
from Estructuras.NodoB import NodoB
import os
class ArbolB:
    def __init__(self):
        self.raiz = None
        self.orden = 5
        self.altura =0
        
    def GetAltura(self):
        return self.altura
    
    def InsertarNodo(self,codigo,nombre,creditos,requisitos,obligatorio):
        nuevo = NodoB(codigo=codigo,nombre=nombre,creditos=creditos,requisitos=requisitos,obligatorio=obligatorio)
        
        if self.raiz == None:
            
            self.raiz = Pagina()
            self.raiz.raiz = True
            self.raiz = self.raiz.Insertar_Pag(nuevo)
           
        else:
            
            if self.altura ==0:#esto es porque no se ha dividido la raiz
                respuesta = self.raiz.Insertar_Pag(nuevo)
                
                if isinstance(respuesta, Pagina):
                    self.raiz = respuesta
                    
                    
                elif isinstance(respuesta,NodoB):
                    self.altura = self.altura+1
                    
                    self.raiz = Pagina()
                    self.raiz = self.raiz.Insertar_Pag(respuesta)
                
            else: #esto es porque la raiz ya se dividio
                respuesta = self.insertar_recorrer(nuevo,self.raiz)
                
                if isinstance(respuesta,NodoB):
                    self.altura = self.altura+1
                    
                    self.raiz  = Pagina()
                    self.raiz = self.raiz.Insertar_Pag(respuesta)
                else:
                    self.raiz = respuesta
    
    
    def insertar_recorrer(self,nuevo,raiz):
        
        
        if raiz.Es_Hoja(raiz):
            respuesta = raiz.Insertar_Pag(nuevo)
            return respuesta
        
        else:
            if nuevo.codigo < raiz.claves.GetPrimero().codigo :
                respuesta = self.insertar_recorrer(nuevo,raiz.claves.GetPrimero().izq)
                
                if isinstance(respuesta, NodoB):
                    return raiz.Insertar_Pag(respuesta)
                else:
                    raiz.claves.GetPrimero().izq = respuesta
                    return raiz
                
            elif nuevo.codigo > raiz.claves.GetUltimo().codigo:
                respuesta = self.insertar_recorrer(nuevo,raiz.claves.GetUltimo().der)
                
                if isinstance(respuesta, NodoB):
                    return raiz.Insertar_Pag(respuesta)
                
                else:
                    raiz.claves.GetUltimo().der = respuesta
                    return raiz
            
            else:
                pivote = raiz.claves.GetPrimero()
                
                while pivote != None:
                    if nuevo.codigo < pivote.codigo:
                        respuesta = self.insertar_recorrer(nuevo,pivote.izq)
                        
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
    
    
    def Recorrer_graficarNodos(self, raiz = Pagina):
        grafo =""
      
        if raiz.Es_Hoja(raiz):
            
            cont =0
            pivote = raiz.claves.GetPrimero()
            grafo +="node"+str(raiz.claves.GetPrimero().codigo)+"[shape=record label= \"<p0>"
            while pivote != None:
                cont = cont+1
                grafo += "|{"+str(pivote.codigo)+ "\\n"+pivote.nombre+"}<p"+str(cont)+">"
                #grafo +="{",pivote.codigo," }<p ",cont,"> "
                pivote = pivote.siguiente  
            
            grafo+="\"]"+"; \n"
            
            return grafo
        else:
            
            grafo+="node"+str(raiz.claves.GetPrimero().codigo)+"[shape=record label= \"<p0>"
            cont =0
            pivote = raiz.claves.GetPrimero()
            
            while pivote != None:
                 cont = cont+1
                 grafo+= "|{"+str(pivote.codigo)+"\\n"+pivote.nombre+" }|<p"+str(cont)+"> "
                 pivote = pivote.siguiente
            
            grafo+="\"]"+"; \n"
            
            pivote = raiz.claves.GetPrimero()
            cont =0
            while pivote != None:
                aux =""
                aux+= self.Recorrer_graficarNodos(pivote.izq)
                grafo+= aux
                cont =cont+1
                pivote = pivote.siguiente
            
            grafo+= self.Recorrer_graficarNodos(raiz.claves.GetUltimo().der)
            
            return grafo
             #seguismo aqui con la graficada
             
    def GraficarArbol(self):
        cadena = "Digraph ArbolB { \n"
        cadena += "rankdir = TB; \n"
        cadena +="node [shape = box,fillcolor=\"azure2\" color=\"black\" style=\"filled\"];\n"
        cadena +=  self.Recorrer_graficarNodos(self.raiz)
        cadena += self.Recorrer_graficarEnlaces(self.raiz)
        cadena += "}"
        Archivo = open("arbolB.dot","w+")
        Archivo.write(cadena)
        Archivo.close()
        
    def Recorrer_graficarEnlaces(self, raiz):
        grafo =""
        if raiz.Es_Hoja(raiz):
            return ""+str(raiz.claves.GetPrimero().codigo )+";"
        else:
            grafo+= ""+str(raiz.claves.GetPrimero().codigo)+";"
            pi = raiz.claves.GetPrimero()
            cont= 0
            r_actual = ""+str(raiz.claves.GetPrimero().codigo)
            while pi != None:
                grafo+= "\n"+str(r_actual)+":p"+str(cont)+"->"+str(self.Recorrer_graficarEnlaces(pi.izq))
                cont =cont+1
                pi = pi.siguiente
            
            grafo+="\n"+r_actual+":p"+str(cont)+"->"+str(self.Recorrer_graficarEnlaces(raiz.claves.GetUltimo().der))
            return grafo
        
     


                    
            
            
