
# coding: utf-8


import numpy as np
from random import randint
from DoubleQuickSort import DoubleQuickSort
from DoubleQuickSort import obtener_numero
from mydijkstra import mydijkstra
import IOCSV as io 
class Aeropuerto:
    indice = None #indice en la lista del grafo
    P = "" ##Tendrá ubicación original archivo
    p = "" ##Tendrá ubicación de paquetes ordenados por archivo
    pos = 0#Tendra la posicion del archivo
    rep = "" ###Tendra el reporte
    aviones = [] #todos los aviones
    paquetes = [] ## todos del mismo destino 
    control = None #grafo
    nombre = None #nombre de este aeropuerto
    terminado = False #cuando acabe el programa
    def __init__(self,graph,indice,P,p,rep):
        self.control = graph
        self.P = P
        self.p = p
        self.rep =rep
        self.indice = indice
    def sortPacks(self):#c
        DoubleQuickSort(self.paquetes)
    def sortOrigins(self): ##ordena el archivo por origenes, los manda a otro  #C
        (lista,pos) = io.rPacks(self.P,"PACK")###leeremos cargamos el archivo a la ram ##ordenamiento externo
        if(pos!=-1):
            print("Algo paso al cargar origins")
            raise
        DoubleQuickSort(lista) ##aqui ordeno para cargarlo al archivo ## ordenamiento externo
        io.wPacks(self.p,lista)
        ##leer del archivo
    def ask4Plane(self):#c
        #Pedir a otros aeropuertos un avión.
        for i in self.control.lista: #Busqueda lineal
            if(len(i.aviones)>3):
                i.sendPlane(self.indice)
                self.control.wPrestamo(self.indice,i.indice)
                return
        print("No se consiguió un avion")
        raise
    def recivePlane(self,avion):##recibirá los aviones #c
        string = avion.toString
        io.wPacks(self.rep,string)
        self.aviones.append(avion)#
    def sendPlane(self,destino): ##sera llamado por una función llamada work #c+-
        avion = self.getPlane()
        if( (not self.terminado)  and (self.paquetes[0].destino == destino)):
            self.fillPlane(avion)
        ## riesgo de que se envién vacios si no esta bien cordinado
        ##calcularemos la mejor ruta con distra
        ruta = mydijkstra(self.control,self.indice,destino)
        avion.ruta = ruta
        try:
            self.control.lista[ruta[len(ruta)]-1].recivePlane(avion)
        except:
            print("problema al send plane")
            raise
        ##Aquí se enviaran los aviones
    def getPlane(self):#c
        if(len(self.aviones)<=0):
            self.ask4Plane()
        try:
            avion = self.aviones.pop()
            avion.fillgas()
            return avion
        except:
            print("problema al sacar avion de la cola")
            raise
    def fillpacks(self):##esta se encargara de que packs este lleno
            #Aquí leere del archivo y se cargará en la ram
            for i in range(len(self.paquetes),101):#Solo 100 paquetes
                
                #pack =Paquetes(datos) leer de archivo
                #pack.bool = True
                self.paquetes.append(1)#aqui leeremos del archivo ##siempre que sea la misma
                
            ##podría ocupar excepciones    
            print("hola")
    def fillPlane(self,avion):
        self.fillpacks()
        self.sortPacks()
        if(len(self.paquetes) == 0):
           self.terminado = True
        peso = 0
        elem = [] #elementos a eliminar
        for i in range(len(self.paquetes)):    
            if(obtener_numero(self.paquetes[i]) + peso <= avion.pesoMax):
                try:
                    avion.addPack(self.paquetes[i])
                    peso+=self.paquetes[i].peso
                    elem.append(self.paquetes[i])
                except:
                    print("Error al sacar un paquete")
                    raise
        for i in reverse()
        
            
        #falta llenar los aviones
    
        

class Paquetes:
    peso = float()
    tamano = float()
    unidad =  float()##da la mejor cantidad  
    nombre = ""
    origen = None
    destino = int()
    bandera = False #si es flaso dará el destino val caracteristico, en otro caso dará la unidad tamaño/peso
    def __init__(self,nombre,peso,tamano,origen,destino):
        self.peso = peso 
        self.tamano = tamano
        self.origen = origen
        self.destino = destino
        self.nombre = nombre
        self.unidad = tamano/peso ##
    def valor_caracteristico(self):
        if(self.bandera):
            return self.unidad
        else:
            return self.destino
    def toString(self):
        #formato:
        #weight,size,destino,nombre
        string = str(self.peso)+str(self.tamano)+str(self.destino)+str(self.nombre)
        return(string)
    
class Avion:
    gas = 1000.0 #se reducirá conforme viaje
    pesoMax = 1999 #kg
    origen = None
    destino = None
    ruta = []
    elementos = [] # debe ser aprovechado
    def __init__(self,origen,destino):
        self.origen = origen
        self.destino = destino
    def fillGas(self):
        self.gas = 1000.0
    def toString(self):
        print("hola")
    def addPack(self,paquete):
        self.elementos.append(paquete)
class Graph:
    matrix = None
    lista = None
    reporte = None
    numAero = None
    nEjes = None
    def __init__(self,numNodes):
        self.matrix = np.zeros((numNodes, numNodes))
        self.lista = np.zeros(numNodes);
        self.numAero = numNodes
    def wPrestamo(self,origen,destino):
        #aqui pondre escribir en el archivo de reportes que se presto un avión
        print("hola")
    def insert_edge(self,intU,intV,intCost,isDirected):
        self.matrix[(intU)][(intV)] = intCost;
        if isDirected == False and intV!=intU:
            self.matrix[(intV)][intU] = intCost;        
    def generador(self): #creará los grafos
        aeropuertos = []
        for i in range(0,self.numAero):
            for j in range(i,self.numAero):
                aeropuertos.append(i)
                aeropuertos.append(j) 
            #aqui hay que crear los aeropuertos
        return aeropuertos
    def create_graph(self):
        #read file
        l = self.generador()
        nEjes = len(l)
        hasCost = True ##
        dirigida = False ## verdadero o falto
        i = 0
        while i < nEjes:
            elem = self.leer(l)
            u = elem.pop(0)
            v = elem.pop(0)
            if hasCost == 1:
                cost = int(randint(1,30)) ## Aquí sea crea el costo
            else:
                cost = 1
            self.insert_edge(u, v, cost,dirigida)
            i += 1
    def printGraph(self):
        for i in self.matrix:
            for j in i():
                print(j)
    def printList(self):
        for i in self.lista:
            print(i.name)
    
############################################
#def print_graph(intMatrix):
#    print (intMatrix)
#
#def create_graph (matrix, hasCost, num_edges,directed):
#    i = 0
#    while i < num_edges :
#        u = int(input('u: '))
#        v = int(input('v: '))
#        if hasCost == True :
#            cost = int(input('Cost / weight: '))
#        else:
#            cost = 1
#        matrix[(u-1)][(v-1)] = cost;
#        if directed == False:
#            matrix[(v-1)][u-1] = cost;
#        i += 1

    

def main():
    print("Numero de nodos")
    num_nodes = int(input())
    print("Tiene costo?")
    hasCost = int(input())
    print("Esta dirigido?")
    directed = int(input())
    directed = True if (directed == 1) else False 
    hasCost = True if (hasCost == 1) else False
    print("Número de ejes?")
    num_edges = int(input())
    matrix = np.zeros((num_nodes, num_nodes))
    create_graph(matrix,hasCost,num_edges,directed)
    print_graph(matrix)

main()

