import time
import numpy as np

def merge_sort(lista):
    if len(lista) > 1:
        mitad = len(lista) // 2
        L = lista[0:mitad]
        R = lista[mitad:]

        merge_sort(L)
        merge_sort(R)

        i=j=k=0

        while i < len(L) and j <len(R):
            if L[i] < R[j]:
                lista[k] = L[i]
                i +=1
            else:
                lista[k] = R[j]
                j += 1
            k +=1

        while i < len(L):
            lista[k] = L[i]
            i +=1
            k += 1

        while j < len(R):
            lista[k] = R[j]
            j += 1
            k += 1

lista = np.random.randn(1,int(1e6)).tolist()[0]
inicio = time.time()
merge_sort(lista)
fin = time.time()
print('El tiempo de ejecución fue', fin-inicio)





