import numpy as np
import time

numeros = np.random.randn(1,int(1e1)).tolist()[0]

def quicksort(start, end, array):
    if start < end:
        p = partition(start,end,array)
        quicksort(start,p-1,array)
        quicksort(p+1,end,array)

def partition(start,end,array):
    pivot_index = start
    pivot = array[pivot_index]

    while start < end:
        while start < len(array) and array[start] <= pivot:
            start +=1

        while array[end] > pivot:
            end -= 1

        if (start < end):
            array[start], array[end] = array[end], array[start]

    array[end], array[pivot_index] = array[pivot_index], array[end]
    return end


print(numeros)
inicio = time.time()
quicksort(0,len(numeros)-1,numeros)
fin = time.time()
print(' \n Tiempo de ejecución:', fin-inicio)





