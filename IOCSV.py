# -*- coding: utf-8 -*-
"""
@author: hectorhmx
"""
import Tabla
import csv
#def rPacks(pwdo,tipo,tam = -1): ##lee y ordena los paquetes no se encarga del origen y destino, ese 
#    try:
#        with open(pwdo, newline='') as entrada:
#            lector = csv.reader(entrada, delimiter=',')
#            lista = []
#            cont = 0
#            for row in lector:
#                if(tam != -1 and cont >= tam ):
#                    return (lista,entrada.tell)
#                else:
#                    cont+=1
#                if(tipo == "PACK"):
#                #self,nombre,peso,tamano,origen,destino
#                #weight,size,destino,nombre
#                # 0      1    2        3
#                    lista.append(Tabla.Paquetes(row[3],float(row[0]),float(row[1]),"",int(row[2]))-1)
#                else:
#                    raise
#            return (lista,-1)
#    except:
#        print("Esta mal el pwd: ",pwdo)
#        raise
       # salida.close()
def rPacks(pwdo,tipo,tam = -1): ##lee y ordena los paquetes no se encarga del origen y destino, ese 
    try:
        with open(pwdo, newline='') as entrada:
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
                #weight,size,destino,nombre,origen
                # 0      1    2        3
                    lista.append(Tabla.Paquetes(row[3],float(row[0]),float(row[1]),0,int(row[2])-1))##aqui se agrega el destino
                else:
                    raise
            return (lista,-1)
    except:
        print("Esta mal el pwd: ",pwdo)
        raise

def rOnePack(pwd,tipo = 0,linea = 0):
    try:
        with open(pwd, newline='') as entrada:
            lector = csv.reader(entrada, delimiter=',')
            for i in range(linea):
                next(lector)
            act = list(next(lector))
            if(len(act) == 0):#EOF
                return ([],-1)
            if(tipo == 0):
                return(act,linea+1)
            if(tipo == act[2]):
                return(act,linea+1)
            else:#end de ese tipo
                return([],linea)
    except StopIteration:
        print("stopped")
        return ([],-1)
    except:
        print("error en OnePack")
        raise



def wPacks(pwds,lista):
    if(len(lista)<1):
        print("Se quiso escribir una lista vacia")
        raise
    else:
        salida = open(pwds,'a+',newline = '')
        escritor = csv.writer(salida, delimiter=',')
        for i in lista:
            if(isinstance(i,Tabla.Paquetes)):
                i.bandera = True
                escritor.writerow(i.toList())
            else:
                escritor.writerow(str(i))

                