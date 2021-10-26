
from Estructuras.ListaMeses import ListaMes
from Estructuras.ListaTareas import listaT
from analizador.sintactico import parser
from Estructuras.AvlAlumnos import AvlAlumno, NodoAlumno
from Estructuras.ListaAños import ListaAño


temporal = listaT()
class carga_masiva():
    def __init__(self):
        pass
    
    
    def Ingresar_estudiante(self,mensaje,Avl):
        resultado = parser.parse(mensaje)
        
        #fds
        for item in resultado:
            if item['type'] == 'user':
                
                carnet_,dpi_,nombre_,carrera_,correo_,pass_ =""," "," "," "," "," "
                edad_,creditos_ =0,0
                contador =0
                for dato in item["atributos"]:
                    if dato.get("Carnet") != None:
                        carnet_ = dato.get("Carnet")
                    if dato.get("DPI") != None:
                        dpi_ = dato.get("DPI")
                    if dato.get("Nombre") != None:
                        nombre_ = dato.get("Nombre")
                    if dato.get("Carrera") != None:
                        carrera_ = dato.get("Carrera")
                    if dato.get("Correo") != None:
                        correo_ = dato.get("Correo")
                    if dato.get("Password") != None:
                        pass_ = dato.get("Password")
                    if dato.get("Edad") != None:
                        edad_ = dato.get("Edad") 
                    if dato.get("Creditos") != None:
                        creditos_ = dato.get("Creditos")   
                        
                    contador = contador+1
                    if contador ==8 :
                        carnet_ = carnet_.replace('\"','')
                        dpi_ =dpi_.replace('\"','')
                        nombre_ =nombre_.replace('\"','')
                        carrera_ =carrera_.replace('\"','')
                        correo_ =correo_.replace('\"','')
                        pass_ =pass_.replace('\"','')
                        
                        
                        Avl.insertar(carnet_,dpi_,nombre_,carrera_,correo_,pass_,creditos_,edad_)
                        print("Estudiante ingresado con exito")
                
    def AsignarRe(self,Avl):
        tt = AvlAlumno()
        pivote = temporal.inicio
        while pivote != None:
            print(pivote.carne)
            
            if tt.Buscar(pivote.carne,tt.raiz) != None:
                alumno = tt.Buscar(pivote.carne,tt.raiz)
                fechas = pivote.fecha.split("/")
                
                if self.ExisteL(alumno.años,fechas(2)) == None:
                    pass
    
    def ExisteL(self,lista,dato):
        ll = ListaAño()
        pi = ll.inicio
        while pi != None:
            if pi.nombre == dato:
                return pi
        
        return None
            

            
            
    
    
    def Ingresar_recordatorio(self,mensaje):
        resultado = parser.parse(mensaje)
        
        
        
        for item in resultado:
            if item['type'] == 'task':
                carnet_,nombre_,descripcion_,materia_,fecha_,hora_,estado_ =" "," "," "," "," "," "," "
                contador =0
                for dato in item["atributos"]:
                    if dato.get("Carnet") != None:
                        carnet_ = dato.get("Carnet")
                    if dato.get("Nombre") != None:
                        nombre_ = dato.get("Nombre")
                    if dato.get("Descripcion") != None:
                        descripcion_ = dato.get("Descripcion")
                    if dato.get("Materia") != None:
                        materia_ = dato.get("Materia")
                    if dato.get("Fecha") != None:
                        fecha_ = dato.get("Fecha")
                    if dato.get("Hora") != None:
                        hora_ = dato.get("Hora")
                    if dato.get("Estado") != None:
                        estado_ = dato.get("Estado")
                    
                    contador = contador+1
                    if contador == 7:
                        carnet_ = carnet_.replace('\"','')
                        nombre_ = nombre_.replace('\"','')
                        descripcion_ = descripcion_.replace('\"','')
                        materia_ = materia_.replace('\"','')
                        fecha_ = fecha_.replace('\"','')
                        hora_ = hora_.replace('\"','')
                        estado_ = estado_.replace('\"','')
                        temporal.insertar(carnet_,nombre_,descripcion_,materia_,fecha_,hora_,estado_)
                        print("Nodo ingresado")
                        
                       # print(carnet_,"--",nombre_,"--",descripcion_,"--",materia_,"--",fecha_,"--",hora_,"--",estado_)
                        
                        
                        
                        
                
                
            
            
            
         
        
       
        
        
                        
        
        
                    
                    
                    

                    
                    
                
                  
                    
                
                
        
        