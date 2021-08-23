#Comparación de valores
i = 5
j = 15
#Retorna es un booelano
i > j
i >= j
i < j
i <= j
i == j
print(i != j)

#Operadores booleanos
a = True
b = False
print(a and b)
print(a or b)

#El condicional
'''
x = float(input('Ingrese un número \n'))
y = float(input('Ingrese otro número \n '))

if x == y:
    print('El número ', x, 'es a igual a ', y)
elif x > y:
    print('El número ', x, ' es mayor que ', y)
else:
    print('El número ', x, ' es menor que', y)
#elif x < y:
#    print('El número ', x, ' es menor que', y)
'''

#Ciclo while
'''
fin = int(input('Ingrese un entero positivo \n') )
suma = 0
j = 1
while j <= fin:
#   suma = suma + j
    suma  += j
    j += 1
print('La suma de los primeros ', fin , ' naturales es ', suma)
'''

#Lo mismo pero con un for
fin = int(input('Ingrese un entero positivo \n') )
suma = 0
for j in range(fin+1):
    suma += j
print('La suma de los primeros ', fin , ' naturales es ', suma)