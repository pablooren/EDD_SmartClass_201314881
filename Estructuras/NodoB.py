class NodoB():
    def __init__(self, codigo,nombre,creditos,requisitos,obligatorio):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
        self.requisitos = requisitos
        self.obligatorio = obligatorio
        
        self.anterior = None
        self.siguiente = None
        self.izq = None
        self.der = None
    