"""
Es un 'arreglo', de longitud variable que tiene elementos de distintas clases.
Las listas SI son mutables. Las listas van entre corchetes
"""

#Creación de una lista vacía
a = []

#Introducir elementos a una lista
a.append(5)

#Imprimir la lista
print(a)

#Función Len
print(len(a))

#La lista es mutable
a[0] = 10
print(a)

#Iteración sobre listas
L = [1,2,3,4,5,6,7,8,9,10]
total = 0
for i in range(len(L)):
    total += L[i]
print(total)

#Otra manera de hacer lo mismo
L = [1,2,3,4,5,6,7,8,9,10]
total = 0
for i in L:
    total += i
print(total)

#Concatenación de listas
L1 = [1,2,3]
L2 = [4,5,6]
print(L1+L2)

#Extender una lista
#L1 = L1 + L2
L1.extend(L2)
print(L1)

#Remover elementos de una lista
print(L1.pop())
print(L1)