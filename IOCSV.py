# -*- coding: utf-8 -*-
"""
@author: hectorhmx
"""
from Tabla import Paquetes
import csv
def rPacks(pwdo,tipo,tam = -1,pos = 0): ##lee y ordena los paquetes no se encarga del origen y destino, ese 
    try:
        with open(pwdo, newline='') as entrada:
            entrada.seek(pos)
            lector = csv.reader(entrada, delimiter=',')
            lista = []
            cont = 0
            for row in lector:
                if(tam != -1 and cont >= tam ):
                    return (lista,entrada.tell)
                else:
                    cont+=1
                if(tipo == "PACK"):
                #self,nombre,peso,tamano,origen,destino
                #weight,size,destino,nombre
                # 0      1    2        3
                    lista.append(Paquetes(row[3],float(row[0]),float(row[1]),"",int(row[2]))-1)
                else:
                    raise
            return (lista,-1)
    except:
        print("Esta mal el pwd: ",pwdo)
        raise
       # salida.close()
       

def wPacks(pwds,lista):
    if(len(lista)<1):
        print("Se quiso escribir una lista vacia")
        raise
    else:
        salida = open(pwds,'a+',newline = '')
        escritor = csv.writer(salida, delimiter=',')
        for i in lista:
            if(isinstance(i,Paquetes)):
                i.bandera = True
                escritor.writerow(i.toString())
            else:
                escritor.writerow(str(i))
                
            
        
                