import numpy as np
import matplotlib.pyplot as imp
from random import randint


#Definición de clases 
class node:
    # edge v
    to = 0
    # weight or cost
    cost = 0
    start = 0
    end = 0
    # Next edge-node
    nxt = None
    
class graph:
    # edges adjacent
    edges = []
    # extern grade
    grade = []
    # nodes number
    num_nodes = 0
    # edges number
    num_edges = 0
    # directed or not
    directed = False

class paquetes:
    peso = float()
    tamano = float()
    nombre = ""
    
class avion:
    gas = 1000.0 #se reducirá conforme viaje
    pesoMax = 100 #kg
    origen = None
    destino = None
    elementos = [] # debe ser aprovechado
    
    

##Definición de Métodos

def start_graph (objGraph,ent):
    objGraph.num_nodes = 0
    objGraph.num_edges = 0
    #print(ent,"Tamaño")
    objGraph.edges = []
    i = 0
    while i<=ent:
        objGraph.grade.append(0)
        objGraph.edges.append(None)
        i += 1
    #print(objGraph.edges,"ejes")
def generador(nodos,caso):
    lista = []
    dirigida = 0
    if(caso == "promedio"):
        ejes = randint(1,(nodos)+1)
        dirigida = randint(0,1)
        #print(dirigida,"su dirección")
        for i in range(1,(ejes)+1):
            lista.append(randint(1,nodos))
            lista.append(randint(1,nodos))
        #print(lista,"lista promedio")
    elif(caso == "peor"):
        dirigida = 0
        for i in range(1,nodos+1):
            for j in range(i+1,nodos+1):
                lista.append(i)
                lista.append(j)   
    else:
        print("Error en la entrada")
        return (None,None,None)
    return (lista,len(lista)//2,dirigida)

def leer(lista):
    u= []
    try:
        u.append(lista.pop(0)) 
        u.append(lista.pop(0)) 
        return u
    except:
        print("entró más de las que debía")
        return -1

def create_graph (objGraph,matrix,caso):
    (l,objGraph.num_edges,dirigida) = generador(objGraph.num_nodes,caso)
    objGraph.directed = True if dirigida == 1 else False
    hasCost = randint(0,1)
    i = 0
    while i < objGraph.num_edges:
        elem = leer(l)
        u = elem.pop(0)
        v = elem.pop(0)
        if hasCost == 1:
            cost = int(randint(1,30))
        else:
            cost = 1
        insert_edge(objGraph, u, v, cost, objGraph.directed,matrix);
        i += 1
        
def insert_edge(objGraph, intU, intV, intCost, isDirected,matrix=-1):
    item = node()
    #print("se conecta",intU,"con",intV)
    item.cost = intCost
    item.to = intV;
    item.nxt = objGraph.edges[intU]
    objGraph.edges[intU] = item
    objGraph.grade[intU] += 1
    if(not isinstance(matrix,int)):
        matrix[(intU-1)][(intV-1)] = intCost;
    if isDirected == False and intV!=intU:
        matrix[(intV-1)][intU-1] = intCost;
        insert_edge(objGraph, intV, intU,intCost,True)
        
def print_graph(objGraph):
    i = 0
    item = None
    string = ""
    while i <= objGraph.num_nodes:
        string += str(i) + "\t"
        item = objGraph.edges[i]
        while item != None:
            string += str(item.to) + ": " + str(item.cost) +"\t"
            item = item.nxt;
        string += "\n"
        i += 1
    print(string)
    print("\n"*3)
    


#def main(caso,tam,maximo):
#    cont = 0
#    ## 1 si es dirigida
#    ##1 si tiene costos
#    num_nodes = tam
#    matrix = np.zeros((num_nodes+1, num_nodes+1))
#    MAXV = num_nodes
#    obj_graph = graph()
#    start_graph(obj_graph,tam) ##empezamos la gráfica
#    obj_graph.num_nodes = num_nodes
#    obj_graph.num_edges = 0
#    create_graph(obj_graph,matrix,caso)
#    cont = DFS(obj_graph,cont)
#    if(tam == maximo):
#        #print(obj_graph.num_edges,"Numero de ejes ultimo caso",caso,obj_graph.num_nodes,"numero de nodos")
#        print_graph(obj_graph)
#        #print(obj_graph.edges[1].to.nxt.to)
#    #BFS(obj_graph,1)
#    return (cont)