"""
Una tupla es una sucesión de elementos de distintas clases
Una característica importante de las tuplas es que son inmutables.
Se representan con paréntesis
"""

#Creación de una tupla
t = ()

#Creando una tupla con elementos
t = (2, "ECFM", 3)

print(t[1])

#Una tupla es inmutable
# Esta operación no está permitida t[1] = "Matemática"

#Se puede concatenar tuplas
t = t + (1,2)

#Imprimir t
print(t)

#Función len
print(len(t))

#Uso interesante de las tuplas
#Para intercambio de valores de variables
x = 5
y = 6
temp = y
y =  x
x = temp

print(x, y)
#Con tuplas es más sencillo
(x,y) = (y,x)
print(x,y)

#Uso interesante para retornar más de un valor en una función

def cociente_residuo(x,y):
    q = x // y #División entera
    r = x % y
    return (q,r)

print(cociente_residuo(20,6))

#Iteración sobre tuplas
def obtener_datos(aTuple):
    nums = ()
    words = ()
    for t in aTuple: #Iterando sobre la tupla
        nums = nums + (t[0], )
        if t[1] not in words:
            words = words + (t[1],)
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return (min_n, max_n, unique_words)

t = ((2,"dos"), (3,"tres"), (4, "dos"))
print(obtener_datos(aTuple=t))