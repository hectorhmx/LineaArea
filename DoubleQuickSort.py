# -*- coding: utf-8 -*-
"""
@author: hectorhmx
"""
from math import ceil
def obtener_numero(dato):
    try:
        mayor = int(dato)
    except:
        try:
            mayor = ord(dato)
        except:
            try:
                temp = 0
                for c in dato:
                    temp += ord(c)
                mayor = temp
            except:
                try:
                    return obtener_numero(dato.valor_caracteristico())
                except:
                    try:
                        cadena = str(dato)
                        return obtener_numero(cadena)
                    except:
                        raise TypeError
    return mayor
# Definimos el algoritmo de ordenamiento con el que vamos a trabajar
cont = 0
def intercambia(A,x,y): #---->C 
#    global cont 
#    cont = cont + 1
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp
def obtenerMedio(A,p,r):
#    global cont
    prom = 0
    for i in A[p : r + 1]:
#        cont = cont + 1
        prom = prom + obtener_numero(i) #obtener numero()"""
    prom = prom // len( A[p : r + 1])
    
    ant = None
    pos = 0
    for i in range(len(A[p : r + 1])):
#        cont = cont + 1
        act = prom - obtener_numero(A[i+p])#"""obtener numero()"""
        if(ant == None or ant > abs(act)):
            ant = abs(act)
            pos = i+p
    return pos
    
def Particionar(A,p,r):
#    global cont
    """
    Aquì hay que poner obtener el medio
    y =  A.index(np.percentile(A[p:r],50,interpolation='nearest')) #n por la api
    """ 
    #if(p == 0 and r == len(A)-1):
    y = obtenerMedio(A,p,r)
    intercambia(A,y,r) #n
    x=A[r] #C
    i=p-1 #C
    for j in range(p,r): #n
        if (obtener_numero(A[j])<=obtener_numero(x)): #C
            i=i+1 #C
            intercambia(A,i,j) #C
#        cont = cont + 1 #C
    intercambia(A,i+1,r) #C
    return i+1 #C

# Por lo tanto es n + n
# Particionar = n

def QuickSortHector(A,p,r): 
#    global cont
    if( p<r ): #C
        q=Particionar(A,p,r) #n
        QuickSortHector(A,p,q-1)# por la separación es log(n)
        QuickSortHector(A,q+1,r)# por la separación es log(n)
#    cont = cont + 1
    
def QuickSortHectorb(arreglo):
#    global tiempo
#    global cont
#    cont = 0
    QuickSortHector(arreglo,0,len(arreglo) - 1)
#    tiempo += cont
#    return cont


# In[71]:


#Algoritmo quick original
def partition(arr,low,high):
#    global tiempo
#    tiempo += 1
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot
    for j in range(low , high):
#        tiempo += 1
        # If current element is smaller than or
        # equal to pivot
        if   obtener_numero(arr[j]) <= obtener_numero(pivot):
         
            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
 
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )
 
def quickSort(arr,low,high):
#    global tiempo
#    tiempo += 1
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

def QuickSort(A):
#    global tiempo
    quickSort(A,0,len(A)-1)
#    return tiempo




def DoubleQuickSort(arreglo):
    contdir = 0
    continv = 0
    for i in range(1,len(arreglo)):
        if(obtener_numero(arreglo[i-1])<=obtener_numero(arreglo[i])):
            contdir+=1
            
    if(contdir==len(arreglo)-1):
        #print("entro")
        return
    #else:
     #   print(contdir,"contador")
      #  print(len(arreglo)-1)
    
    for i in range(1,len(arreglo)):
        if(obtener_numero(arreglo[i-1])>=obtener_numero(arreglo[i])):
            continv+=1
            
    if(continv == len(arreglo)-1):
        for i in range(0,ceil(len(arreglo)/2)):
            aux = arreglo[i]
            arreglo[i] = arreglo[len(arreglo) - 1 - i]
            arreglo[len(arreglo) - 1-i] = aux
        return
    cerc = 1.7 ##Nos dirá que tanto se aproximará a el valor esperado
    if(continv >= (len(arreglo)-1)//cerc or contdir >= (len(arreglo)-1)//cerc):
        QuickSortHectorb(arreglo)
    else:
        QuickSort(arreglo)


