# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


####################
## EJEMPLO: Método para encontrar la raíz cúbica de un número positivo
####################
cubo = 1.5
epsilon = 0.01
numero_intentos = 0
low = 0.0
high = cubo
numero_prueba = (high + low)/2.0
while abs(numero_prueba**3 - cubo) >= epsilon:
    if numero_prueba**3 < cubo:
        low = numero_prueba
    else:
        high = numero_prueba
    numero_prueba = (high + low)/2.0
    print(numero_prueba)
    numero_intentos += 1
print('El número de iteraciones fue =', numero_intentos)
print(numero_prueba, 'es aproximadamente la raíz cúbica de ', cubo)
