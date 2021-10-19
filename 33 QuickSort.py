import numpy as np
import time
from math import floor
import sys
sys.setrecursionlimit(1500000)
numeros = np.random.randint(low=-1000,high=1000, size=1000000)
numeros_ordenados = numeros.copy()
numeros_ordenados.sort()

def quicksort(start, end, array):
    if start < end:
        p = partition(start,end,array)
        if p < start:
            print("Error", p, start, end)
        quicksort(start,p-1,array)
        quicksort(p+1,end,array)

def partition(start,end,array):
    pivot_index = floor( (start + end) / 2 )
    pivot = array[pivot_index]
    inicio = start

    while start < end:
        while  array[start] <= pivot and start < len(array)-1:
            start +=1

        while array[end] >= pivot and end >= inicio:
            end -= 1

        if (start < end):
            array[start], array[end] = array[end], array[start]

    retorno = 0
    if end > pivot_index:
        retorno = end
        array[pivot_index], array[end] = array[end], array[pivot_index]
    else:
        retorno = end+1
        array[pivot_index], array[end+1] = array[end+1], array[pivot_index]

    return retorno


inicio = time.time()
quicksort(0,len(numeros)-1,numeros)
fin = time.time()
print(' \n Tiempo de ejecución:', fin-inicio)
if (numeros == numeros_ordenados).all():
    print(True)




