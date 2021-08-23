import time

inicio = time.time()
limite = 10001
contador = 0
entero = 2
while contador < limite-1:
    #verifica si entero es primo o no
    for x in range(2,entero):
        if entero % x == 0:
            break
        if x == (entero-1):
            contador +=1
    entero +=1
final = time.time()
print(entero-1, 'El tiempo de ejecución es ', final - inicio)
