
# coding: utf-8


import numpy as np
from random import randint
from DoubleQuickSort import DoubleQuickSort
import IOCSV as io 
class Aeropuerto:
    indice = None
    P = "" ##Tendrá ubicación original archivo
    p = "" ##Tendrá ubicación de paquetes ordenados por archivo
    rep = "" ###Tendra el reporte
    aviones = []
    paquetes = []
    control = None
    nombre = None
    def __init__(self,graph,indice,P,p,rep):
        self.control = graph
        self.P = P
        self.p = p
        self.rep =rep
        self.indice = indice
    def sortPacks(self):#c
        DoubleQuickSort(self.paquetes)
    def sortOrigins(self): ##ordena el archivo por origenes, los manda a otro  #C
        (lista,pos) = io.rPacks(self.P,"PACK")###leeremos cargamos el archivo a la ram
        if(pos!=-1):
            print("Algo paso al cargar origins")
            raise
        DoubleQuickSort(lista)
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
    def recivePlane(self,avion):##recibirá los aviones
        string = avion.stoString
        if(len(avion.elementos) > 0):
            io.wPacks(self.rep,string)
        self.aviones.append(avion)#
    def sendPlane(self,destino):
            print("hola")
            ##Aquí se enviaran los aviones
    def getPlane(self):
        if(len(self.aviones>0)):
            avion = self.aviones.pop()
            avion.fillgas()
        else:
            avion = self.ask4Plane()
        return avion
    def fillpacks(self):
            #Aquí leere del archivo y se cargará en la ram
            for i in range(len(self.paquetes),101):#Solo 100 paquetes
                
                #pack =Paquetes(datos) leer de archivo
                #pack.bool = True
                self.paquetes.append(1)#aqui leeremos del archivo ##siempre que sea la misma
                
            ##podría ocupar excepciones    
            self.sortPacks()
            print("hola")
    def fillPlane(self,avion):
        avion = self.getPlane()
        self.fillpacks()
        ###DoubleQuickSort()
        return avion
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
    elementos = [] # debe ser aprovechado
    def __init__(self,origen,destino):
        self.origen = origen
        self.destino = destino
    def fillGas(self):
        self.gas = 1000.0
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

