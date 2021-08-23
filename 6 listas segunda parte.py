#Convertir una cadena en una lista
cadena = 'Hola Mundo'
lista_cadena = list(cadena)
print(lista_cadena)

#Convertir una lista en una cadena
cadena_convertida = ''.join(lista_cadena)
print(cadena_convertida)

#Ordenamientos
num = [2,34,1232,5432,3,4,5,2234,4]
num.sort()
print(num)

#Reverse
num = [2,34,1232,5432,3,4,5,2234,4]
num.reverse()
print(num)

#Alias en las listas
a = list(range(100))
b = a #b es un alias de a (pasa a por referencia, no por valor)
a.reverse()
print('La lista a es ', a)
print('La lista b es ', b)

#Copias de una lista
a = list(range(100))
b = a[:] #permite crear una copia de la lista
a.reverse()
print('La lista a es ', a)
print('La lista b es ', b)

#Las listas permiten anidación (para formar matrices)
matriz_unitaria = [[1,0],[0,1]]
print(matriz_unitaria[1][1])

#List comprehension
cuadrados = []
for x in range(1,11):
    cuadrados.append(x**2)
print(cuadrados)

#Versión corta
cuadrados2 = [i**2 for i in range(1,11)]
print(cuadrados2)