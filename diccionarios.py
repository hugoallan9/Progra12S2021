#Crear un diccionario
num = {"Uno":1, "Dos":2, "Tres":3}

#Agregar un elemento
num["Cuatro"] = 4

print(num)

#Verificar si una llave forma parte o no del diccionario
print('Cuatro' in num)
print('Cinco' in num)

#Borrar entrada del diccionario
del(num["Cuatro"])
print(num)

#Iterar sobre el diccionario
for x in  num.keys():
    print(x)

for x in num.values():
    print(x)

#Ejemplos de uso de un diccionario
def frecuencia_cadena(cadena):
    diccionario_conteo = {}
    for palabra in cadena.split():
        if palabra in diccionario_conteo:
            diccionario_conteo[palabra] +=1
        else:
            diccionario_conteo[palabra] = 1
    return diccionario_conteo

cadena = "Your Butt Is Mine \
Gonna Take You Right \
Just Show Your Face \
In Broad Daylight\
I\'m Telling You"

print(frecuencia_cadena(cadena))