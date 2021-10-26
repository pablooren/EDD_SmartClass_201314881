from Estructuras.listaB import Lista_NodoB

class Pagina:
    def __init__(self):
        self.claves = Lista_NodoB()
        self.max = 4
        self.min = 2
        self.tamaño = 0
        self.raiz = False
        
    def Insertar_Pag(self,Nodob):
        self.claves.Insertar(Nodob)
        self.tamaño = self.claves.GetTamaño()
       
        
        if self.tamaño < 5:
           
            return self
        
        elif self.tamaño == 5:
          
            return self.dividir_pag(self)
        
        
    def dividir_pag(self, pag):
        temp = pag.claves.GetPrimero()
        temp = temp.siguiente.siguiente
        
        
        primero = pag.claves.GetPrimero()
        segundo = primero.siguiente
       
        cuarto = temp.siguiente
        quinto = pag.claves.GetUltimo()
        primero.siguiente = None
        primero.anterior = None
         
        segundo.siguiente = None
        segundo.anterior = None
        
        quinto.siguiente = None
        quinto.anterior = None
        
        cuarto.siguiente = None
        cuarto.anterior = None
        
        temp.siguiente = None
        temp.anterior = None
        
        pagina_izq = Pagina()
        pagina_izq.Insertar_Pag(primero)
        pagina_izq.Insertar_Pag(segundo)
        
        
        pagina_der = Pagina()
        pagina_der.Insertar_Pag(cuarto)
        pagina_der.Insertar_Pag(quinto)
        
        temp.izq = pagina_izq
        temp.der = pagina_der
        return temp
    
        
    def Es_Hoja(self,pag ):
        pi = pag.claves.GetPrimero()
        if pi.izq == None:
            return True
        else:
            return False
    
    
