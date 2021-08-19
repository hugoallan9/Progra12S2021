import time

inicio = time.time()
limite = 10001
lista_primos = [2]
entero = 3
while len(lista_primos) < limite:
    #verifica si entero es primo o no
    for x in lista_primos:
        if entero % x == 0:
            break
        if x == lista_primos[-1]:
            lista_primos.append(entero)
    entero +=1
final = time.time()
print(entero-1, 'El tiempo de ejecución es ', final - inicio)
