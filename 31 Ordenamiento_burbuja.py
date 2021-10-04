import numpy as np
import time

numeros = np.random.randn(1,int(1e6)).tolist()[0]



def burbuja(lista):
    for recorrido in range(len(lista)-1,0,-1):
        for i in range(recorrido):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]




inicio = time.time()
burbuja(numeros)
fin = time.time()
print(' \n Tiempo de ejecución:', fin-inicio)
