import time
import math
from funcion_primo import is_prime


inicio = time.time()
limite = 10001
contador = 1
entero = 3
while contador < limite-1:
    #verifica si entero es primo o no
    if is_prime(entero):
        contador += 1
    entero +=1
final = time.time()
print(entero-1, 'El tiempo de ejecución es ', final - inicio)
