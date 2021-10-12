from Estructuras.MatrizTareas import Matriz_ortogonal
from Estructuras.ListaTareas import listaT
import os


nueva_matriz = Matriz_ortogonal()

lista = listaT()
lista.insertar("201314881","Juan","Tarea loca","EDD","14/10/1994","12","completa")
lista.insertar("201314881","Pablo","Tarea loca","EDD","14/10/1994","12","completa")
lista.insertar("201314881","orellana","Tarea loca","EDD","14/10/1994","12","completa")
lista.insertar("201314881","penate","Tarea loca","EDD","14/10/1994","12","completa")


#arreglemos para que los datos de la matriz vengan ya ordenados en x osea dias
nueva_matriz.insertar(3,14,lista)
nueva_matriz.insertar(3,11,lista)
nueva_matriz.insertar(3,17,lista)

nueva_matriz.insertar(5,14,lista)
nueva_matriz.insertar(12,14,lista)

print(nueva_matriz.buscar(3,17))

nodo = nueva_matriz.NodoRaiz.NodoFilas


while(nodo is not None):
    nodo_temp = nodo.derecha
    while(nodo_temp is not None):
        print("x:  "+str(nodo_temp.x)+ ", y:  "+str(nodo_temp.y))
        nodo_temp.recordatorios.MostarT()
        
        nodo_temp=nodo_temp.derecha
    nodo=nodo.siguiente
    
print("FIN Recorrido 1")
nodo = nueva_matriz.NodoRaiz.NodoColumnas
while(nodo is not None):
    nodo_temp = nodo.abajo
    while(nodo_temp is not None):
        print("x:  "+str(nodo_temp.x)+ ", y:  "+str(nodo_temp.y))
        nodo_temp=nodo_temp.abajo
    nodo=nodo.siguiente
    
print("FIN Recorrido 2")


def graficar_matriz():
    grafo = "digraph"
    grafo+=str("{\nnode[shape=record];\n")
    grafo+=str("graph[pencolor=transparent];\n")
    #grafo+=str("rankdir=LR;\n")
    grafo+=str("node [style=filled];\n")
    nodo = nueva_matriz.NodoRaiz.NodoFilas

    for y in range(1, 11):
        nodo_temp = nodo.derecha
        for x in range(1, 11):
            if(nueva_matriz.buscar(x,y)):
                grafo+=str("p"+str(x)+str(y)+"[label=\"{<data>"+str(x)+","+str(y)+"|<next>}\" pos=\""+str(x)+","+str(10-y)+"!\"];\n")
                if(nodo_temp.derecha!=None): 
                    nodo_2=nodo_temp
                    nodo_temp=nodo_temp.derecha
                    grafo+=str("p"+str(nodo_2.x)+str(nodo_2.y)+"->"+"p"+str(nodo_temp.x)+str(nodo_temp.y)+"[dir=both];\n")
            else:
                pass
            if nodo.siguiente!=None:
                if nodo.siguiente.indice==y+1:
                    nodo=nodo.siguiente    
    nodo = nueva_matriz.NodoRaiz.NodoColumnas
    for x in range(1, 11):
        nodo_temp = nodo.abajo
        for y in range(1, 11):
            if(nueva_matriz.buscar(x,y)):
                if(nodo_temp.abajo!=None):
                    nodo_2=nodo_temp
                    nodo_temp=nodo_temp.abajo
                    grafo+=str("p"+str(nodo_2.x)+str(nodo_2.y)+"->"+"p"+str(nodo_temp.x)+str(nodo_temp.y)+"[dir=both];\n")
            else:
                pass
            if nodo.siguiente!=None:
                if nodo.siguiente.indice==x+1:
                    nodo=nodo.siguiente         
    grafo+=str("}\n")
    f= open("ejemplo.dot","w+")
    f.write(grafo)
    f.close() 
    print("********* Se realizo Grafica *********  ")  
   # os.system("fdp -Tpng -o graph-g.png ejemplo.dot")


#graficar_matriz()