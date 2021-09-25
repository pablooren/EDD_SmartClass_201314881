from listaB import Lista_NodoB

class Pagina:
    def __init__(self, claves = Lista_NodoB):
        self.claves = claves
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
            return dividir_pag(self)
        
        
    def dividir_pag(self, pag):
        temp = pag.claves.getPrimero()
        temp = temp.siguiente.siguiente
        
        primero = pag.claves.getPrimero()
        segundo = primero.siguiente
        tercero = temp.siguiente
        cuarto = pag.claves.GetUltimo()
        
        primero.siguiente = None
        primero.anterior = None
         
        segundo.siguiente = None
        segundo.anterior = None
        
        tercero.siguiente = None
        tercero.anterior = None
        
        cuarto.siguiente = None
        cuarto.anterior = None
        
        temp.siguiente = None
        temp.anterior = None
        list1 = Lista_NodoB
        pagina_izq = Pagina(list1)
        pagina_izq.Insertar_Pag(primero.codigo,primero.nombre)
        pagina_izq.Insertar_Pag(segundo.codigo,tercero.nombre)
        list2 = Lista_NodoB
        pagina_der = Pagina(list2)
        pagina_der.Insertar_Pag(tercero.codigo,tercero.nombre)
        pagina_der.Insertar_Pag(cuarto.codigo,cuarto.nombre)
        
        temp.izq = pagina_izq
        temp.der = pagina_der
        
        return temp
    
        
    def Es_Hoja(self,pag ):
        if pag.claves.getPrimero().izq == None:
            return True
        else:
            return False
    
    
